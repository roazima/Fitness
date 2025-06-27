from fastapi import APIRouter, Body
from app.mock_openai import parse_food_input
from kafka_producer import send_to_kafka
import json

router = APIRouter()

@router.get("/")
def health_check():
    return {"message": "App is running!"}
@router.post("/log-food")   
def log_food(input: str = Body(...)):
    result = parse_food_input(input)    # Get the parsed JSON
    send_to_kafka(result)               # Fire and forget (no need to store return)
    return result                       # Return parsed data to user

