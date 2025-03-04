from pydantic import BaseModel

class UserProfile(BaseModel):
    experience_level: str
    goals: str