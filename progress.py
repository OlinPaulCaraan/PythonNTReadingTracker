# progress.py

import json
import os
from books import new_testament

PROGRESS_FILE = "progress.json"

def initialize_progress():
    # Create or reset progress file with all chapters unread (False)
    if not os.path.exists(PROGRESS_FILE):
        progress = {}
        for book, chapters in new_testament.items():
            progress[book] = [False] * chapters
        with open(PROGRESS_FILE, "w") as f:
            json.dump(progress, f, indent=4)

def load_progress():
    # Load progress from JSON file
    with open(PROGRESS_FILE, "r") as f:
        return json.load(f)

def save_progress(progress):
    # Save progress dictionary back to JSON file
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=4)
