"""
Resume data models.

Simple dataclasses for structured resume data. No external dependencies.
"""

from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class Contact:
    name: str
    email: str
    phone: str = ""
    location: str = ""
    preferred_name: Optional[str] = None
    linkedin: Optional[str] = None
    website: Optional[str] = None


@dataclass
class WorkEntry:
    title: str
    company: str
    dates: str
    bullets: list[str] = field(default_factory=list)
    url: Optional[str] = None
    description: Optional[str] = None


@dataclass
class ProjectEntry:
    title: str
    dates: str
    bullets: list[str] = field(default_factory=list)
    url: Optional[str] = None
    description: Optional[str] = None


@dataclass
class EducationEntry:
    degree: str
    institution: str
    dates: str
    bullets: list[str] = field(default_factory=list)
    url: Optional[str] = None


@dataclass
class ResumeData:
    contact: Contact
    work: list[WorkEntry] = field(default_factory=list)
    projects: list[ProjectEntry] = field(default_factory=list)
    education: list[EducationEntry] = field(default_factory=list)
    skills: dict[str, list[str]] = field(default_factory=dict)
    summary: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "ResumeData":
        """Create ResumeData from dictionary."""
        return cls(
            contact=Contact(**data.get("contact", {})),
            work=[WorkEntry(**w) for w in data.get("work", [])],
            projects=[ProjectEntry(**p) for p in data.get("projects", [])],
            education=[EducationEntry(**e) for e in data.get("education", [])],
            skills=data.get("skills", {}),
            summary=data.get("summary"),
        )
