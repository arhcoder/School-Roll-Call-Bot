import os
import csv
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
    # Load existing users from the CSV file:
    existing_users = []
    try:
        with open("users.csv", "r", newline="") as file:
            reader = csv.reader(file)
            existing_users = list(reader)
    except FileNotFoundError:
        pass

    # Check if userid already exists:
    user_exists = any(user[0] == userid for user in existing_users)
    # If it exists, updates the row:
    if user_exists:
        for user in existing_users:
            if user[0] == userid:
                user[1] = username
                user[2] = password
                break
    # If not, it appends:
    else:
        existing_users.append([userid, username, password])

    # Write the updated/added users back to the CSV file:
    with open("users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(existing_users)

def get_users(filename="users.csv"):
    users = []
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                users.append({
                    "userid": row[0],
                    "username": row[1],
                    "password": row[2]
                })
    except FileNotFoundError:
        print(f"File \"{filename}\" not found.")
    return users