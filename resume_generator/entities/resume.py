from pydantic import BaseModel, Field

from .certification import Certification
from .contact import Contact
from .education import Education
from .language import Language
from .skill import Skill
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
    languages: list[Language] = Field(default_factory=list)
    certifications: list[Certification] = Field(default_factory=list)
    skills: list[Skill] = Field(default_factory=list)

    def get_calculated_skills(self, gt_years: int = 3) -> list[dict[str, str | int]]:
        _skills = {}
        for exp in self.work_experience:
            for tool in exp.tools:
                if tool not in _skills:
                    _skills[tool] = 0
                _skills[tool] += (exp.end_date_obj - exp.start_date_obj).days

        _sorted = dict(sorted(_skills.items(), key=lambda item: item[1], reverse=True))

        return [
            {"name": k, "years": round(v / 365)}
            for k, v in _sorted.items()
            if v // 365 >= gt_years
        ]
