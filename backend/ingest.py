"""
Resume ingestion utilities.

Provides persona management functions. The ingestion pipeline itself
is now handled by the AI agent directly.
"""

import os
from pathlib import Path
from typing import Union
import yaml
import json
import argparse
import sys
from .models import ResumeData
from .generator import generate_typst, compile_pdf, check_page_count


# Project root
PROJECT_ROOT = Path(__file__).parent.parent
PERSONAS_DIR = PROJECT_ROOT / "personas"


def update_current_persona(persona: str, role: str) -> None:
    """Update .current_persona file."""
    current_file = PROJECT_ROOT / ".current_persona"
    current_file.write_text(f"{persona} {role}\n")


def get_current_persona() -> tuple[str, str]:
    """Get current persona and role from .current_persona file."""
    current_file = PROJECT_ROOT / ".current_persona"
    if not current_file.exists():
        return "davy", "pm"  # Default
    
    parts = current_file.read_text().strip().split()
    if len(parts) >= 2:
        return parts[0], parts[1]
    return parts[0] if parts else "davy", "pm"


def ingest_resume_from_json(
    json_path: Union[str, Path],
    persona_name: str,
    role: str,
    template: str = "modern"
) -> dict:
    """
    Ingest resume from a JSON file (agent-driven).
    
    1. Validates JSON against ResumeData schema
    2. Enforces existing persona constraints (optional)
    3. Generates Typst source
    4. Compiles PDF
    5. Updates current persona
    
    Args:
        json_path: Path to the JSON file containing parsed resume data
        persona_name: Name of the persona (e.g. "davy")
        role: Role identifier (e.g. "pm")
        template: Template to use
        
    Returns:
        Result dictionary with paths and status
    """
    json_path = Path(json_path)
    if not json_path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")
        
    # 1. Load and Validate Data
    try:
        data_dict = json.loads(json_path.read_text())
        resume_data = ResumeData.from_dict(data_dict)
    except Exception as e:
        raise ValueError(f"Invalid resume JSON: {e}")
        
    # 2. Setup Persona Directory
    persona_dir = PERSONAS_DIR / persona_name
    persona_dir.mkdir(parents=True, exist_ok=True)
    
    # Ensure config exists
    config_path = persona_dir / "config.yaml"
    if not config_path.exists():
        config = {
            "name": resume_data.contact.name,
            "preferred_name": resume_data.contact.preferred_name or resume_data.contact.name.split()[0],
            "default_role": role,
            "has_career_profile": False
        }
        with open(config_path, "w") as f:
            yaml.dump(config, f)
            
    # 3. Generate Typst
    typ_filename = f"{persona_name}_{role}_master_resume.typ"
    typ_path = persona_dir / typ_filename
    
    typ_content = generate_typst(resume_data, template)
    typ_path.write_text(typ_content)
    
    # 4. Compile PDF
    pdf_path = compile_pdf(typ_path)
    
    # 5. Check Pages
    page_count = check_page_count(pdf_path)
    
    # 6. Update Current
    update_current_persona(persona_name, role)
    
    return {
        "status": "success",
        "persona": persona_name,
        "role": role,
        "typ_file": str(typ_path),
        "pdf_file": str(pdf_path),
        "page_count": page_count
    }
def list_personas() -> list[dict]:
    """List all available personas and their roles."""
    personas = []
    
    if not PERSONAS_DIR.exists():
        return personas
    
    for persona_dir in PERSONAS_DIR.iterdir():
        if not persona_dir.is_dir():
            continue
        
        persona_name = persona_dir.name
        roles = []
        
        # Find all role-specific resumes
        for typ_file in persona_dir.glob("*_master_resume.typ"):
            # Extract role from filename: {persona}_{role}_master_resume.typ
            parts = typ_file.stem.replace("_master_resume", "").split("_")
            if len(parts) >= 2:
                role = parts[-1]  # Last part before _master_resume
                roles.append(role)
        
        # Load config
        config_path = persona_dir / "config.yaml"
        config = {}
        if config_path.exists():
            with open(config_path) as f:
                config = yaml.safe_load(f) or {}
        
        personas.append({
            "name": persona_name,
            "display_name": config.get("name", persona_name.title()),
            "preferred_name": config.get("preferred_name", persona_name.title()),
            "roles": roles,
            "default_role": config.get("default_role", roles[0] if roles else None),
            "has_career_profile": config.get("has_career_profile", False),
        })
    
    return personas


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resume Ingestion Utility")
    parser.add_argument("--json", help="Path to JSON resume data")
    parser.add_argument("--persona", help="Persona name")
    parser.add_argument("--role", help="Role identifier")
    parser.add_argument("--template", default="modern", help="Resume template")
    
    args = parser.parse_args()
    
    if args.json and args.persona and args.role:
        # Ingestion mode
        try:
            result = ingest_resume_from_json(args.json, args.persona, args.role, args.template)
            print(json.dumps(result, indent=2))
        except Exception as e:
            print(json.dumps({"status": "error", "message": str(e)}, indent=2))
            sys.exit(1)
    else:
        # List mode (default)
        print("Available personas:")
        for p in list_personas():
            print(f"  - {p['name']} [{', '.join(p['roles'])}]")
        
        current = get_current_persona()
        print(f"\nCurrent: {current[0]} ({current[1]})")
