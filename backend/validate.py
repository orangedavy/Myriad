import sys
import fitz
import json
from backend.monitor import detect_runts

def validate_resume(pdf_path):
    print(f"🔍 Validating: {pdf_path}")
    
    # 1. Page Count Check
    try:
        doc = fitz.open(pdf_path)
        page_count = len(doc)
        if page_count > 1:
            print(f"❌ FAILURE: Page count is {page_count} (Limit: 1)")
            print("   👉 Action: Shorten bullets or remove skills.")
            return False
        else:
            print(f"✅ Page Count: {page_count}")
    except Exception as e:
        print(f"❌ ERROR: Could not open PDF for validation: {e}")
        return False

    # 2. Runt Check (Warning only)
    try:
        runts = detect_runts(pdf_path)
        if runts:
            print(f"⚠️ WARNING: {len(runts)} potential runts found:")
            for runt in runts:
                print(f"   - Page {runt['page']}: \"{runt['text']}\"")
            print("   👉 Action: Tweaking wording slightly to fix.")
        else:
            print("✅ No runts detected.")
    except Exception as e:
        print(f"⚠️ WARNING: Runt detection failed: {e}")
    
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m backend.validate <pdf_path>")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    success = validate_resume(pdf_path)
    
    if not success:
        sys.exit(1)
    sys.exit(0)
