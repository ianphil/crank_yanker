from pydantic import BaseModel, field_validator

class UserProfile(BaseModel):
    experience_level: str
    goals: str

    @field_validator("experience_level", "goals")
    def check_not_empty(cls, v):
        if not v:
            raise ValueError("Field cannot be empty")
        return v