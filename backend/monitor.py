"""
Monitor for resume quality issues (runts/orphans, overflow).
"""

import fitz  # PyMuPDF
import re

def detect_runts(pdf_path: str, threshold_chars: int = 15) -> list[dict]:
    """
    Detect lines that are "runts" (orphans) - very short final lines of paragraphs.
    
    Args:
        pdf_path: Path to PDF
        threshold_chars: Lines shorter than this are considered runts
        
    Returns:
        List of dicts identifying the page and content of runts
    """
    doc = fitz.open(pdf_path)
    runts = []
    
    for page_num, page in enumerate(doc):
        # proper extraction of text blocks relative to layout
        blocks = page.get_text("blocks")
        
        for block in blocks:
            text = block[4].strip()
            # Split into lines (this assumes visual lines map roughly to \\n or block logic)
            # PyMuPDF block text often groups paragraph content. 
            # We need a better heuristic: check the length of the *last line* of the block.
            
            # Re-fetch as dict to get individual spans/lines if needed, 
            # but simple newline splitting on text blocks works for most simple PDFs
            lines = text.split('\n')
            
            if not lines:
                continue
                
            last_line = lines[-1].strip()
            
            # Check if it's a runt:
            # 1. It must be short
            # 2. It shouldn't be a standalone bullet that is naturally short (like a skill or date)
            #    We test this by checking if the PREVIOUS line was "full".
            #    Actually, simpler heuristic: if it's < threshold and not a bullet point marker.
            
            if 0 < len(last_line) <= threshold_chars:
                # Filter out obvious non-runts
                if re.match(r'^[\u2022\-\*]\s*$', last_line): 
                    continue # Just a bullet marker
                if re.match(r'^\d{4}\s*[\u2013\-]\s*(Present|\d{4})$', last_line):
                    continue # Date range
                # Filter out section headings
                if last_line in ['Work', 'Education', 'Skills', 'Projects', 'Experience', 'Summary']:
                    continue
                # Filter out names (title case, 2-3 words)
                if re.match(r'^[A-Z][a-z]+(\s+[A-Z][a-z]+){0,2}$', last_line):
                    continue
                    
                context = lines[-2] if len(lines) > 1 else ""
                runts.append({
                    "page": page_num + 1,
                    "text": last_line,
                    "context": context[-50:] + " " + last_line
                })
                
    return runts


def check_page_fill(pdf_path: str) -> dict:
    """
    Check how much of the page is filled with content.
    
    Returns dict with:
        - fill_percent: Approximate percentage of page used
        - warning: True if <60% filled
        - suggestion: Recommendation if sparse
    """
    doc = fitz.open(pdf_path)
    if len(doc) == 0:
        return {"fill_percent": 0, "warning": True, "suggestion": "Empty document"}
    
    page = doc[0]
    page_height = page.rect.height
    
    # Get bounding box of all content
    blocks = page.get_text("blocks")
    if not blocks:
        return {"fill_percent": 0, "warning": True, "suggestion": "No text content"}
    
    # Find content bounds
    max_y = max(block[3] for block in blocks)  # bottom
    min_y = min(block[1] for block in blocks)  # top
    
    content_height = max_y - min_y
    fill_percent = (content_height / page_height) * 100
    
    result = {
        "fill_percent": round(fill_percent, 1),
        "warning": fill_percent < 60,
        "suggestion": None
    }
    
    if fill_percent < 40:
        result["suggestion"] = "Resume is very sparse. Consider adding more content."
    elif fill_percent < 60:
        result["suggestion"] = "Resume has significant whitespace. Consider adding content or reducing margins."
    
    return result
