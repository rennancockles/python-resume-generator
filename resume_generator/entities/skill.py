from pydantic import BaseModel


class Skill(BaseModel):
    """
    Represents a skill entry in a resume.
    """

    name: str
    years: int = 0
