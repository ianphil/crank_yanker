import logging
from pathlib import Path

# Configure logging
LOG_FILE = Path("agent.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # Also log to console for debugging
    ]
)
logger = logging.getLogger(__name__)

def handle_error(e: Exception) -> None:
    """Log an exception and display a friendly message to the user."""
    logger.error(f"Error occurred: {str(e)}", exc_info=True)
    print(f"Oops! Something went wrong: {str(e)}. Check agent.log for details.")