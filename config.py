"""
Configuration file containing all settings and credentials.
"""

# API Configuration
TOKEN = "TOKEN"
ENDPOINT = "https://models.inference.ai.azure.com"
MODEL_NAME = "gpt-4o"

# Processing Configuration
MAX_RETRIES = 5
INITIAL_WAIT_TIME = 61  # seconds
TEMPERATURE = 0.75
MAX_TOKENS = 3000
BASE_FOLDER = "Benchmark"

# Output Configuration
OUTPUT_COLUMNS = ["File Name", "Question", "Response"]
