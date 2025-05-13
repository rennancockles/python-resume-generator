from pydantic import BaseModel

from .certification import Certification
from .contact import Contact
from .education import Education
from .language import Language
from .work_experience import WorkExperience


class Resume(BaseModel):
    """
    Represents a resume.
    """

    name: str
    title: str
    summary: str
    education: list[Education]
    work_experience: list[WorkExperience]
    contact: Contact
    languages: list[Language]
    certifications: list[Certification]
