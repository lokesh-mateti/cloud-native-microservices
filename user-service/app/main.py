from fastapi import FastAPI
from typing import List

app = FastAPI(title="User Service")

users_db = [
    {"id": 1, "name": "Lokesh"},
    {"id": 2, "name": "DevOps Engineer"}
]

@app.get("/health")
def health_check():
    return {"status": "UP"}

@app.get("/users", response_model=List[dict])
def get_users():
    return users_db
