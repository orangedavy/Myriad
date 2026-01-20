"""
Convert parsed resume data to Typst format.

Generates a complete Typst file from ResumeData that can be compiled to PDF.
"""

import subprocess
from pathlib import Path
from typing import Union

from .models import ResumeData, Contact, WorkEntry, ProjectEntry, EducationEntry


# Template directory
TEMPLATE_DIR = Path(__file__).parent.parent / "typst" / "templates"

AVAILABLE_TEMPLATES = ["modern"]


def _escape_typst(text: str) -> str:
    """Escape special Typst characters."""
    if not text:
        return ""
    # Escape characters that have special meaning in Typst
    replacements = [
        ("\\", "\\\\"),
        ("#", "\\#"),
        ("$", "\\$"),
        ("@", "\\@"),
        ("<", "\\<"),
        (">", "\\>"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def _format_contact(contact: Contact) -> str:
    """Generate Typst content for contact section."""
    lines = []
    lines.append(f'    name: "{_escape_typst(contact.name)}",')
    lines.append(f'    email: "{_escape_typst(contact.email)}",')
    
    if contact.preferred_name:
        lines.append(f'    preferred_name: "{_escape_typst(contact.preferred_name)}",')
    if contact.phone:
        lines.append(f'    phone: "{_escape_typst(contact.phone)}",')
    if contact.location:
        lines.append(f'    location: "{_escape_typst(contact.location)}",')
    if contact.linkedin:
        lines.append(f'    linkedin: "{_escape_typst(contact.linkedin)}",')
    if contact.website:
        lines.append(f'    website: "{_escape_typst(contact.website)}",')
    
    return "\n".join(lines)


def _format_work(work: list[WorkEntry]) -> str:
    """Generate Typst content for work section."""
    if not work:
        return "  work: (),"
    
    entries = []
    for job in work:
        bullets = ", ".join(f'"{_escape_typst(b)}"' for b in job.bullets)
        entry = f'''    (
      title: "{_escape_typst(job.title)}",
      company: "{_escape_typst(job.company)}",
      url: {f'"{job.url}"' if job.url else 'none'},
      description: {f'"{_escape_typst(job.description)}"' if job.description else 'none'},
      dates: "{_escape_typst(job.dates)}",
      bullets: ({bullets}),
    )'''
        entries.append(entry)
    
    return "  work: (\n" + ",\n".join(entries) + ",\n  ),"


def _format_projects(projects: list[ProjectEntry]) -> str:
    """Generate Typst content for projects section."""
    if not projects:
        return "  projects: (),"
    
    entries = []
    for proj in projects:
        bullets = ", ".join(f'"{_escape_typst(b)}"' for b in proj.bullets)
        entry = f'''    (
      title: "{_escape_typst(proj.title)}",
      url: {f'"{proj.url}"' if proj.url else 'none'},
      description: {f'"{_escape_typst(proj.description)}"' if proj.description else 'none'},
      dates: "{_escape_typst(proj.dates)}",
      bullets: ({bullets}),
    )'''
        entries.append(entry)
    
    return "  projects: (\n" + ",\n".join(entries) + ",\n  ),"


def _format_education(education: list[EducationEntry]) -> str:
    """Generate Typst content for education section."""
    if not education:
        return "  education: (),"
    
    entries = []
    for edu in education:
        bullets = ", ".join(f'"{_escape_typst(b)}"' for b in edu.bullets)
        entry = f'''    (
      degree: "{_escape_typst(edu.degree)}",
      institution: "{_escape_typst(edu.institution)}",
      url: {f'"{edu.url}"' if edu.url else 'none'},
      dates: "{_escape_typst(edu.dates)}",
      bullets: ({bullets}),
    )'''
        entries.append(entry)
    
    return "  education: (\n" + ",\n".join(entries) + ",\n  ),"


def _format_skills(skills: dict[str, list[str]]) -> str:
    """Generate Typst content for skills section."""
    if not skills:
        return "  skills: (:),"
    
    entries = []
    for category, items in skills.items():
        item_str = ", ".join(f'"{_escape_typst(i)}"' for i in items)
        entries.append(f'    "{_escape_typst(category)}": ({item_str})')
    
    return "  skills: (\n" + ",\n".join(entries) + "\n  ),"


def generate_typst(
    data: ResumeData,
    template: str = "modern",
    output_path: Union[str, Path, None] = None,
) -> str:
    """
    Generate Typst file content from ResumeData.
    
    Args:
        data: Parsed resume data
        template: Template name (modern, classic, minimal)
        output_path: Optional path to write the file
        
    Returns:
        Generated Typst content as string
    """
    if template not in AVAILABLE_TEMPLATES:
        raise ValueError(f"Unknown template: {template}. Available: {AVAILABLE_TEMPLATES}")
    
    # Build data dictionary for template
    typst_content = f'''// Generated Resume - {template.title()} Template
// Edit personal information in the data dictionary below

#import "../../typst/templates/{template}.typ": render

#let data = (
  contact: (
{_format_contact(data.contact)}
  ),
  summary: {f'"{_escape_typst(data.summary)}"' if data.summary else 'none'},
{_format_work(data.work)}
{_format_projects(data.projects)}
{_format_education(data.education)}
{_format_skills(data.skills)}
)

#render(data)
'''
    
    if output_path:
        Path(output_path).write_text(typst_content)
    
    return typst_content


def generate_letter_typst(
    data: ResumeData,
    body: str,
    output_path: Union[str, Path, None] = None,
    recipient: dict = None,
) -> str:
    """
    Generate Typst Cover Letter content.
    """
    # Build data dictionary
    # We need to construct the 'recipient' dict string manually
    recipient_str = "none"
    if recipient:
        lines = []
        for k, v in recipient.items():
            lines.append(f'    {k}: "{_escape_typst(v)}",')
        recipient_str = "(\n" + "\n".join(lines) + "\n  )"

    typst_content = f'''// Generated Cover Letter
#import "../../../typst/templates/letter.typ": render

#let data = (
  contact: (
{_format_contact(data.contact)}
  ),
  date: none, // Uses today's date by default
  recipient: {recipient_str},
  body: "{_escape_typst(body)}",
)

#render(data)
'''
    
    if output_path:
        Path(output_path).write_text(typst_content)
    
    return typst_content


def compile_pdf(
    typst_path: Union[str, Path],
    output_path: Union[str, Path, None] = None,
) -> tuple[bool, str]:
    """
    Compile Typst file to PDF.
    
    Args:
        typst_path: Path to the .typ file
        output_path: Optional custom output path for PDF
        
    Returns:
        Tuple of (success, message)
    """
    typst_path = Path(typst_path).resolve()
    
    if output_path is None:
        output_path = typst_path.with_suffix(".pdf")
    else:
        output_path = Path(output_path).resolve()
    
    try:
        # Determine project root
        project_root = Path(__file__).parent.parent.resolve()
        
        # When running typst, we set root to project_root
        result = subprocess.run(
            ["typst", "compile", "--root", str(project_root), str(typst_path), str(output_path)],
            capture_output=True,
            text=True,
            cwd=project_root,  # Run from root to avoid confusion, since we pass absolute paths
        )
        
        if result.returncode == 0:
            return True, f"PDF generated: {output_path}"
        else:
            return False, f"Compilation failed: {result.stderr}"
            
    except FileNotFoundError:
        return False, "Typst not installed. Install with: brew install typst"


def check_page_count(pdf_path: Union[str, Path]) -> int:
    """
    Check the number of pages in a PDF.
    
    Uses PyMuPDF for counting.
    """
    import fitz  # PyMuPDF
    
    with fitz.open(pdf_path) as doc:
        return len(doc)


def generate_and_compile(
    data: ResumeData,
    output_dir: Union[str, Path],
    persona: str,
    role: str,
    template: str = "modern",
) -> tuple[bool, str, Path]:
    """
    Full pipeline: generate Typst and compile to PDF.
    
    Args:
        data: Parsed resume data
        output_dir: Directory to save files
        persona: Persona name (e.g., "davy")
        role: Role name (e.g., "pm")
        template: Template name
        
    Returns:
        Tuple of (success, message, pdf_path)
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    filename = f"{persona}_{role}_master_resume"
    typst_path = output_dir / f"{filename}.typ"
    pdf_path = output_dir / f"{filename}.pdf"
    
    # Generate Typst
    typst_content = generate_typst(data, template, typst_path)
    
    # Compile to PDF
    success, message = compile_pdf(typst_path, pdf_path)
    
    if success:
        # Check page count
        pages = check_page_count(pdf_path)
        if pages > 1:
            return False, f"Resume is {pages} pages. One-page limit exceeded.", pdf_path
    
    return success, message, pdf_path


if __name__ == "__main__":
    # Quick test with sample data
    sample = ResumeData(
        contact=Contact(
            name="John Doe",
            email="john@example.com",
            phone="555-1234",
            location="Seattle, WA",
        ),
        work=[
            WorkEntry(
                title="Software Engineer",
                company="TechCorp",
                dates="2020 – Present",
                bullets=["Built stuff", "Led teams"],
            )
        ],
        education=[
            EducationEntry(
                degree="BS Computer Science",
                institution="University of Washington",
                dates="2016 – 2020",
            )
        ],
        skills={"Technical": ["Python", "JavaScript", "SQL"]},
    )
    
    print(generate_typst(sample, "modern"))
