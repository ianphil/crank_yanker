import json
from typing import Optional
from pathlib import Path
from cycling_agent.models import UserProfile

STATE_FILE = Path("user_state.json")

def save_user_data(user_profile: UserProfile) -> None:
    """Save the user profile to a JSON file."""
    with STATE_FILE.open("w") as f:
        json.dump(user_profile.dict(), f, indent=4)

def load_user_data() -> Optional[UserProfile]:
    """Load the user profile from a JSON file if it exists."""
    if STATE_FILE.exists():
        with STATE_FILE.open("r") as f:
            data = json.load(f)
            return UserProfile(**data)
    return None