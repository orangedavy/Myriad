"""Resume Builder Backend - Utility tools for resume processing."""

# Text extraction
from .extractors import extract_text

# Data models
from .models import ResumeData, Contact, WorkEntry, ProjectEntry, EducationEntry

# Typst generation & PDF compilation
from .generator import (
    generate_typst,
    generate_letter_typst,
    compile_pdf,
    check_page_count,
    AVAILABLE_TEMPLATES,
)
# Resume quality monitoring
from .monitor import detect_runts, check_page_fill

# Persona management
from .ingest import list_personas, update_current_persona, ingest_resume_from_json

__all__ = [
    # Extraction
    'extract_text',
    # Generation
    'generate_typst',
    'generate_letter_typst',
    'compile_pdf',
    'check_page_count',
    'AVAILABLE_TEMPLATES',
    # Monitoring
    'detect_runts',
    'check_page_fill',
    # Personas
    'list_personas',
    'update_current_persona',
    'ingest_resume_from_json',
]
