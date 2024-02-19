import os
import json
from dotenv import load_dotenv
from encrypt import encode

#/ ENV SECRETS:
load_dotenv()
TOKEN = os.getenv("TOKEN")
KEY = os.getenv("KEY")

#/ USERS FUNCTIONS:
def save_user(userid, username, password):
    # Encodes the password to save it:
    password = encode(password, KEY)
    
    # Load existing users from the JSON file:
    existing_users = []
    try:
        with open("users.json", "r") as file:
            existing_users = json.load(file)
    except FileNotFoundError:
        pass

    # Check if userid already exists:
    user_exists = any(user["userid"] == userid for user in existing_users)
    # If it exists, updates the user:
    if user_exists:
        for user in existing_users:
            if user["userid"] == userid:
                user["username"] = username
                user["password"] = password
                break
    # If not, appends a new user:
    else:
        existing_users.append({"userid": userid, "username": username, "password": password})

    # Write the updated/added users back to the JSON file:
    with open("users.json", "w") as file:
        json.dump(existing_users, file)

def get_users(filename="users.json"):
    users = []
    try:
        with open(filename, "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print(f"File \"{filename}\" not found.")
    return users