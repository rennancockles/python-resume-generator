from contextlib import suppress
from datetime import date, datetime

from pydantic import BaseModel, Field


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
    tools: list[str] = Field(default_factory=list)

    @property
    def start_date_obj(self) -> date:
        if not self.start_date:
            return date.today()

        with suppress(ValueError):
            return datetime.strptime(self.start_date, "%Y").date()

        with suppress(ValueError):
            return datetime.strptime(self.start_date, "%Y-%m").date()

        raise ValueError(
            f"Invalid end date format: {self.start_date}. "
            "Expected formats: YYYY or YYYY-MM."
        )

    @property
    def end_date_obj(self) -> date:
        if not self.end_date:
            return date.today()

        with suppress(ValueError):
            return datetime.strptime(self.end_date, "%Y").date()

        with suppress(ValueError):
            return datetime.strptime(self.end_date, "%Y-%m").date()

        raise ValueError(
            f"Invalid end date format: {self.end_date}. "
            "Expected formats: YYYY or YYYY-MM."
        )
