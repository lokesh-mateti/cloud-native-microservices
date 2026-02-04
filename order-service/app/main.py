from fastapi import FastAPI
import requests
import os

app = FastAPI(title="Order Service")

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service:8080")

@app.get("/health")
def health():
    return {"status": "UP"}

@app.get("/orders")
def get_orders():
    users = requests.get(f"{USER_SERVICE_URL}/users").json()

    return {
        "orders": [
            {"order_id": 101, "user": users[0]["name"], "item": "Laptop"},
            {"order_id": 102, "user": users[1]["name"], "item": "Headphones"}
        ]
    }
