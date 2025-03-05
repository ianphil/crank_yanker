import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pathlib import Path
from cycling_agent.state_manager import save_user_data, load_user_data
from cycling_agent.models import UserProfile

@pytest.fixture
def mock_state_file(tmp_path):
    state_file = tmp_path / "user_state.json"
    with state_file.open("w") as f:
        f.write('{"experience_level": "intermediate", "goals": "racing"}')
    yield state_file

def test_save_user_data(tmp_path, monkeypatch):
    monkeypatch.setattr("cycling_agent.state_manager.STATE_FILE", tmp_path / "user_state.json")
    profile = UserProfile(experience_level="beginner", goals="fitness")
    save_user_data(profile)
    assert (tmp_path / "user_state.json").exists()

def test_load_user_data(mock_state_file, monkeypatch):
    monkeypatch.setattr("cycling_agent.state_manager.STATE_FILE", mock_state_file)
    profile = load_user_data()
    assert profile.experience_level == "intermediate"
    assert profile.goals == "racing"

def test_load_user_data_no_file(tmp_path, monkeypatch):
    monkeypatch.setattr("cycling_agent.state_manager.STATE_FILE", tmp_path / "nonexistent.json")
    profile = load_user_data()
    assert profile is None