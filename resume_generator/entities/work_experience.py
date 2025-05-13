from pydantic import BaseModel


class WorkExperience(BaseModel):
    """
    Represents a work experience entry in a resume.
    """

    start_date: str
    end_date: str = ""
    location: str
    remote: bool = False
    company: str
    title: str
    description: str = ""
    tools: str = ""
