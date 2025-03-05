import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cycling_agent.models import UserProfile
from pydantic import ValidationError

def test_user_profile_valid():
    profile = UserProfile(experience_level="beginner", goals="fitness")
    assert profile.experience_level == "beginner"
    assert profile.goals == "fitness"

def test_user_profile_invalid():
    try:
        UserProfile(experience_level="", goals="")
        assert False, "Should raise ValidationError for empty strings"
    except ValidationError:
        assert True