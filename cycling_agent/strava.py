import os
# Uncomment the following line when ready to use real API
# import requests

def authenticate():
    """Stub or placeholder for Strava authentication."""
    print("Authenticating with Strava...")
    # Placeholder for real authentication
    # client_id = os.getenv("STRAVA_CLIENT_ID")
    # client_secret = os.getenv("STRAVA_CLIENT_SECRET")
    # refresh_token = os.getenv("STRAVA_REFRESH_TOKEN")
    # if not all([client_id, client_secret, refresh_token]):
    #     raise ValueError("Missing Strava credentials in environment variables")
    # # Add OAuth2 flow here to get access token

def fetch_metrics():
    """Fetch Strava metrics, using stub if real API not configured."""
    authenticate()
    
    # Placeholder for real Strava API call
    # access_token = "your_access_token"  # Replace with actual token from authenticate()
    # headers = {"Authorization": f"Bearer {access_token}"}
    # response = requests.get("https://www.strava.com/api/v3/athlete/activities", headers=headers)
    # if response.status_code == 200:
    #     data = response.json()
    #     latest_activity = data[0]  # Assuming latest activity
    #     return {
    #         "distance": latest_activity.get("distance", 0) / 1000,  # Convert meters to km
    #         "heart_rate": latest_activity.get("average_heartrate", 0),
    #         "power": latest_activity.get("average_watts", 0)
    #     }
    # else:
    #     print(f"Strava API error: {response.status_code}")
    
    # Stubbed fallback
    return {
        "distance": 30,  # kilometers
        "heart_rate": 150,  # beats per minute
        "power": 180  # watts
    }