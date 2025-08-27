from dotenv import dotenv_values  # Loads key-value pairs from a .env file into a dictionary
import os # Provides utilities for file and path manipulation

# Construct the absolute path to the zen.env file
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'zen.env'))

# Load all environment variables from the .env file
config = dotenv_values(env_path)

# Extract values from the config
BASE_URL = config.get("BASE_URL", "").strip()
USERNAME = config.get("USERNAME", "").strip()
PASSWORD = config.get("PASSWORD", "").strip()
HEADLESS = config.get("HEADLESS", "false").strip().lower() == "true"