from typing import Annotated

from pydantic import BaseModel, EmailStr, HttpUrl, StringConstraints


class Address(BaseModel):
    """
    Represents an address entry in a resume.
    """

    line1: str = ""
    line2: str = ""


class Phone(BaseModel):
    """
    Represents a phone entry in a resume.
    """

    number: str = ""
    whatsapp: bool = False


class Contact(BaseModel):
    """
    Represents a contact entry in a resume.
    """

    address: Address
    phone: Phone
    email: EmailStr | Annotated[str, StringConstraints(max_length=0)] = ""
    website: HttpUrl | Annotated[str, StringConstraints(max_length=0)] = ""
    linkedin: HttpUrl | Annotated[str, StringConstraints(max_length=0)] = ""
    github: HttpUrl | Annotated[str, StringConstraints(max_length=0)] = ""
