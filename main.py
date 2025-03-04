import click
from cycling_agent.models import UserProfile
from pydantic import ValidationError
from cycling_agent.state_manager import load_user_data, save_user_data

def prompt_for_profile():
    """Prompt user for profile data and return a UserProfile."""
    while True:
        try:
            experience_level = click.prompt("Your cycling experience level (e.g., beginner, intermediate, advanced)")
            goals = click.prompt("Your cycling goals (e.g., fitness, racing, leisure)")
            profile = UserProfile(experience_level=experience_level, goals=goals)
            return profile
        except ValidationError as e:
            click.echo("Invalid input detected:")
            click.echo(e)
            click.echo("Please try again.\n")

@click.command()
def create_profile():
    """Create or load a user profile for the Cycling Agent."""
    # Try to load existing user data
    user_profile = load_user_data()

    if user_profile:
        # Greet user with existing data
        click.echo(f"Welcome back!")
        click.echo(f"Experience Level: {user_profile.experience_level}")
        click.echo(f"Goals: {user_profile.goals}")
    else:
        # No data exists, prompt for new profile
        click.echo("No existing profile found. Let's create one.")
        user_profile = prompt_for_profile()
        
        # Save the new profile
        save_user_data(user_profile)
        
        # Confirm save and display profile
        click.echo("Profile created and saved successfully!")
        click.echo(f"Experience Level: {user_profile.experience_level}")
        click.echo(f"Goals: {user_profile.goals}")

if __name__ == '__main__':
    create_profile()