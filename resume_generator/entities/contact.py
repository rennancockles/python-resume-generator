from typing import Annotated, Union

from pydantic import BaseModel, EmailStr, HttpUrl, StringConstraints


class Address(BaseModel):
    """
    Represents an address entry in a resume.
    """

    line1: str
    line2: str = ""


class Phone(BaseModel):
    """
    Represents a phone entry in a resume.
    """

    number: str
    whatsapp: bool = False


class Contact(BaseModel):
    """
    Represents a contact entry in a resume.
    """

    address: Address
    phone: Phone
    email: Union[EmailStr, Annotated[str, StringConstraints(max_length=0)]] = ""
    website: Union[HttpUrl, Annotated[str, StringConstraints(max_length=0)]] = ""
    linkedin: Union[HttpUrl, Annotated[str, StringConstraints(max_length=0)]] = ""
    github: Union[HttpUrl, Annotated[str, StringConstraints(max_length=0)]] = ""
