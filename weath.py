import requests
import pandas as pd
import time
from datetime import datetime

# Define coordinates for Kathmandu and Pokhara
locations = [
    {"city": "Kathmandu", "latitude": 27.7172, "longitude": 85.3240},
    {"city": "Pokhara", "latitude": 28.2096, "longitude": 83.9856}
]

# Initialize dictionaries to store weather data for each city
weather_data = {
    "Kathmandu": [],
    "Pokhara": []
}

# Define the Open-Meteo API URL
api_url = "https://api.open-meteo.com/v1/forecast"