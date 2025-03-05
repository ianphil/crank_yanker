import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cycling_agent.workout_generator import calculate_power_zones, generate_weekly_plan
from cycling_agent.models import UserProfile

def test_calculate_power_zones():
    zones = calculate_power_zones(200)
    assert zones["Z1"] == (0, 110)
    assert zones["Z2"] == (112, 150)
    assert zones["Z3"] == (152, 180)
    assert zones["Z4"] == (182, 210)
    assert zones["Z5"] == (212, 240)

def test_generate_weekly_plan_beginner():
    profile = UserProfile(experience_level="beginner", goals="fitness")
    zones = calculate_power_zones(200)
    metrics = {"distance": 15, "heart_rate": 140, "power": 150}
    plan = generate_weekly_plan(profile, zones, metrics)
    assert len(plan) == 4  # Base 3 + 1 adjustment
    assert any(session["intensity"] == "Z2" and "Build endurance" in session["description"] for session in plan)

def test_generate_weekly_plan_advanced_racing():
    profile = UserProfile(experience_level="advanced", goals="racing")
    zones = calculate_power_zones(300)
    metrics = {"distance": 50, "heart_rate": 180, "power": 250}
    plan = generate_weekly_plan(profile, zones, metrics)
    assert len(plan) == 8  # Base 5 + recovery (distance) + recovery (HR) + VO2 max
    assert any("VO2 max intervals" in session["description"] for session in plan)