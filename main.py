from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

USER_DB = "users.json"

class User(BaseModel):
    username: str
    password: str

def load_users():
    try:
        with open(USER_DB, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f)

@app.post("/register")
def register(user: User):
    users = load_users()
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.username] = user.password
    save_users(users)
    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: User):
    users = load_users()
    if users.get(user.username) == user.password:
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
