import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Get a list of subdirectories in the base directory
subdirectories = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]

# Print the list of subdirectories
print(subdirectories)
