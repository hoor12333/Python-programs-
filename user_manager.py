import json
import os

# ------------------------------
# Save data to a JSON file
# ------------------------------
def save_user(data, filename="users.json"):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


# ------------------------------
# Load data from a JSON file
# ------------------------------
def load_users(filename="users.json"):
    if not os.path.exists(filename):
        return []  # If no file exists, return empty list

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: File is not valid JSON.")
        return []
    except Exception as e:
        print(f"Error loading file: {e}")
        return []
