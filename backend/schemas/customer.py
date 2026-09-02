from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class CustomerCreate(BaseModel):
    full_name: str = Field(
        min_length=2,
        max_length=200,
    )

    email: EmailStr

    phone: str = Field(
        min_length=10,
        max_length=30,
    )


class CustomerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    email: EmailStr
    phone: str
    created_at: datetime