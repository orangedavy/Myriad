"""
Resume ingestion utilities.

Provides persona management functions. The ingestion pipeline itself
is now handled by the AI agent directly.
"""

import os
from pathlib import Path
from typing import Union
import yaml


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
    print("Available personas:")
    for p in list_personas():
        print(f"  - {p['name']} [{', '.join(p['roles'])}]")
    
    current = get_current_persona()
    print(f"\nCurrent: {current[0]} ({current[1]})")
