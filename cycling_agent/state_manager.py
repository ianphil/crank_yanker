import json
from typing import Optional
from pathlib import Path
from cycling_agent.models import UserProfile
from cycling_agent.error_handler import logger, handle_error

STATE_FILE = Path("user_state.json")

def save_user_data(user_profile: UserProfile) -> None:
    """Save the user profile to a JSON file."""
    try:
        with STATE_FILE.open("w") as f:
            json.dump(user_profile.model_dump(), f, indent=4)  # Changed from dict() to model_dump()
        logger.info("User profile saved successfully.")
    except Exception as e:
        handle_error(e)

def load_user_data() -> Optional[UserProfile]:
    """Load the user profile from a JSON file if it exists."""
    try:
        if STATE_FILE.exists():
            with STATE_FILE.open("r") as f:
                data = json.load(f)
                profile = UserProfile(**data)
                logger.info("User profile loaded successfully.")
                return profile
        logger.info("No existing user profile found.")
        return None
    except Exception as e:
        handle_error(e)
        return None