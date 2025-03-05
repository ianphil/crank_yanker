from pydantic import BaseModel, constr

class UserProfile(BaseModel):
    experience_level: constr(min_length=1)  # Ensures string is not empty
    goals: constr(min_length=1)