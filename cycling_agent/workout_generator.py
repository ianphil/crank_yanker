from typing import Dict, List
from cycling_agent.models import UserProfile

def calculate_power_zones(ftp: int) -> Dict[str, tuple]:
    """Calculate basic power zones based on Functional Threshold Power (FTP)."""
    return {
        "Z1": (0, int(ftp * 0.55)),       # Active Recovery: < 55% FTP
        "Z2": (int(ftp * 0.56), int(ftp * 0.75)),  # Endurance: 56-75% FTP
        "Z3": (int(ftp * 0.76), int(ftp * 0.90)),  # Tempo: 76-90% FTP
        "Z4": (int(ftp * 0.91), int(ftp * 1.05)),  # Threshold: 91-105% FTP
        "Z5": (int(ftp * 1.06), int(ftp * 1.20))   # VO2 Max: 106-120% FTP
    }

def generate_weekly_plan(user_profile: UserProfile, zones: Dict[str, tuple], metrics: dict) -> List[dict]:
    """Generate a weekly training plan based on user profile, zones, and Strava metrics."""
    plan = []
    
    # Base plan based on experience level
    if user_profile.experience_level.lower() == "beginner":
        plan.extend([
            {"day_of_week": "Monday", "duration": "1h", "intensity": "Z1", "description": "Easy recovery ride"},
            {"day_of_week": "Wednesday", "duration": "1h", "intensity": "Z2", "description": "Endurance ride"},
            {"day_of_week": "Saturday", "duration": "1.5h", "intensity": "Z2", "description": "Longer endurance ride"},
        ])
    elif user_profile.experience_level.lower() == "intermediate":
        plan.extend([
            {"day_of_week": "Monday", "duration": "1h", "intensity": "Z1", "description": "Recovery ride"},
            {"day_of_week": "Tuesday", "duration": "1h", "intensity": "Z3", "description": "Tempo intervals"},
            {"day_of_week": "Thursday", "duration": "1.5h", "intensity": "Z2", "description": "Endurance ride"},
            {"day_of_week": "Saturday", "duration": "2h", "intensity": "Z3", "description": "Long tempo ride"},
        ])
    else:  # Advanced
        plan.extend([
            {"day_of_week": "Monday", "duration": "1h", "intensity": "Z1", "description": "Recovery ride"},
            {"day_of_week": "Tuesday", "duration": "1.5h", "intensity": "Z4", "description": "Threshold intervals"},
            {"day_of_week": "Thursday", "duration": "2h", "intensity": "Z3", "description": "Tempo endurance"},
            {"day_of_week": "Friday", "duration": "1h", "intensity": "Z2", "description": "Easy spin"},
            {"day_of_week": "Sunday", "duration": "3h", "intensity": "Z2", "description": "Long endurance ride"},
        ])

    # Adjust plan based on Strava metrics
    if metrics["distance"] < 20:  # Recent ride was short
        plan.append({"day_of_week": "Friday", "duration": "1.5h", "intensity": "Z2", 
                     "description": f"Build endurance (noted your recent {metrics['distance']}km ride)"})
    elif metrics["distance"] > 40:  # Recent ride was long
        plan.append({"day_of_week": "Wednesday", "duration": "1h", "intensity": "Z1", 
                     "description": f"Extra recovery (after your recent {metrics['distance']}km ride)"})

    if metrics["heart_rate"] > 170:  # High effort recently
        plan.append({"day_of_week": "Tuesday", "duration": "45m", "intensity": "Z1", 
                     "description": f"Light recovery (your HR hit {metrics['heart_rate']} bpm)"})

    if "racing" in user_profile.goals.lower():
        plan.append({"day_of_week": "Wednesday", "duration": "1h", "intensity": "Z5", 
                     "description": f"VO2 max intervals (power noted at {metrics['power']}W)"})

    return plan