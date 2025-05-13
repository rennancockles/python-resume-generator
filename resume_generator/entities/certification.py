from typing import Annotated, Union

from pydantic import BaseModel, HttpUrl, StringConstraints


class Certification(BaseModel):
    """
    Represents a certification entry in a resume.
    """

    date: str
    authority: str
    name: str
    url: Union[HttpUrl, Annotated[str, StringConstraints(max_length=0)]] = ""
