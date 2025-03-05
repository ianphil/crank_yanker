import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from click.testing import CliRunner
from main import create_profile

@pytest.fixture
def runner():
    return CliRunner()

def test_create_profile_new_user(runner, tmp_path, monkeypatch):
    monkeypatch.setattr("cycling_agent.state_manager.STATE_FILE", tmp_path / "user_state.json")
    result = runner.invoke(create_profile, input="beginner\nfitness\n200\n")
    assert result.exit_code == 0
    assert "Profile created and saved successfully!" in result.output
    assert "Your Weekly Training Plan:" in result.output

def test_create_profile_existing_user(runner, tmp_path, monkeypatch):
    state_file = tmp_path / "user_state.json"
    with state_file.open("w") as f:
        f.write('{"experience_level": "intermediate", "goals": "racing"}')
    monkeypatch.setattr("cycling_agent.state_manager.STATE_FILE", state_file)
    result = runner.invoke(create_profile, input="200\n")
    assert result.exit_code == 0
    assert "Welcome back!" in result.output
    assert "Your Weekly Training Plan:" in result.output

def test_full_session_integration(runner, tmp_path, monkeypatch):
    monkeypatch.setattr("cycling_agent.state_manager.STATE_FILE", tmp_path / "user_state.json")
    # First run: new user
    result = runner.invoke(create_profile, input="intermediate\nracing\n250\n")
    assert result.exit_code == 0
    assert "Profile created and saved successfully!" in result.output
    assert "Strava Metrics:" in result.output
    assert "Your Weekly Training Plan:" in result.output

    # Second run: existing user
    result = runner.invoke(create_profile, input="250\n")
    assert result.exit_code == 0
    assert "Welcome back!" in result.output
    assert "Your Weekly Training Plan:" in result.output