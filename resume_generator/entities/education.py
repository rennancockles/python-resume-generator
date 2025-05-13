from pydantic import BaseModel


class Education(BaseModel):
    """
    Represents an education entry in a resume.
    """

    start_date: str
    end_date: str
    location: str
    title: str
    institution: str
