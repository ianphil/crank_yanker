import click
from pydantic import ValidationError
from cycling_agent.models import UserProfile
from cycling_agent.state_manager import load_user_data, save_user_data
from cycling_agent.strava import authenticate, fetch_metrics
from cycling_agent.workout_generator import calculate_power_zones, generate_weekly_plan
from cycling_agent.error_handler import logger, handle_error

def prompt_for_profile():
    """Prompt user for profile data and return a UserProfile."""
    while True:
        try:
            experience_level = click.prompt("Your cycling experience level (e.g., beginner, intermediate, advanced)")
            goals = click.prompt("Your cycling goals (e.g., fitness, racing, leisure)")
            profile = UserProfile(experience_level=experience_level, goals=goals)
            logger.info("User profile input validated successfully.")
            return profile
        except ValidationError as e:
            handle_error(e)
            click.echo("Please try again.\n")

@click.command()
def create_profile():
    """Create or load a user profile, fetch Strava data, and generate a workout plan."""
    logger.info("Starting Cycling Agent CLI...")
    try:
        # Try to load existing user data
        user_profile = load_user_data()

        if user_profile:
            click.echo(f"Welcome back!")
            click.echo(f"Experience Level: {user_profile.experience_level}")
            click.echo(f"Goals: {user_profile.goals}")
        else:
            click.echo("No existing profile found. Let's create one.")
            user_profile = prompt_for_profile()
            save_user_data(user_profile)
            click.echo("Profile created and saved successfully!")
            click.echo(f"Experience Level: {user_profile.experience_level}")
            click.echo(f"Goals: {user_profile.goals}")

        # Fetch Strava metrics
        metrics = fetch_metrics()
        click.echo("Strava Metrics:")
        click.echo(f"Distance: {metrics['distance']} km")
        click.echo(f"Heart Rate: {metrics['heart_rate']} bpm")
        click.echo(f"Power: {metrics['power']} watts")

        # Prompt for FTP and generate workout plan
        ftp = click.prompt("Enter your FTP (Functional Threshold Power) in watts", type=int)
        zones = calculate_power_zones(ftp)
        weekly_plan = generate_weekly_plan(user_profile, zones, metrics)

        # Display power zones
        click.echo("\nYour Power Zones:")
        for zone, (low, high) in zones.items():
            click.echo(f"{zone}: {low}-{high} watts")

        # Display weekly plan
        click.echo("\nYour Weekly Training Plan:")
        for session in weekly_plan:
            click.echo(f"{session['day_of_week']}: {session['duration']} at {session['intensity']} - {session['description']}")

        logger.info("Program completed successfully.")
    except Exception as e:
        handle_error(e)

if __name__ == '__main__':
    create_profile()