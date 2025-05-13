from enum import StrEnum

from pydantic import BaseModel


class LanguageLevel(StrEnum):
    """
    Enum for language proficiency levels.
    """

    BASIC = "Basic"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    FLUENT = "Fluent"
    NATIVE = "Native"


class Language(BaseModel):
    """
    Represents a language entry in a resume.
    """

    language: str
    level: LanguageLevel = LanguageLevel.BASIC
