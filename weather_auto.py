from datetime import datetime
import time
import requests
import schedule
import pandas as pd
 
locations = [
    {
        "city": "Pokhara", 
        "latitude": 28.2096,
        "longitude": 83.9856,
    },
    {
        "city": "Kathmandu",
        "latitude": 27.7103,
        "longitude": 85.3222,
    },
    {
        "city": "Dharan",
        "latitude": 26.8065,
        "longitude": 87.2847,
    },
    {
        "city": "Birendranagar",
        "latitude": 28.5952,
        "longitude": 81.6097,
    },
]
 
weather_data = {
    "Pokhara" : [],
    "Kathmandu" : [],
    "Dharan": [],
    "Birendranagar" : []
}
 
def get_weather(location):
 
    url = "https://api.open-meteo.com/v1/forecast"
 
    params = {
        "latitude": location['latitude'],
        "longitude": location['longitude'],	
        "current_weather": "true"
    }
 
    response = requests.get(url, params)
 
    if response.status_code == 200:
        data = response.json().get('current_weather')
        if data:
            data ['city'] = location['city']
            data['timestamp'] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
 
            city_name = location['city']
            weather_data[city_name].append(data)
            print("Data fetched for city", city_name)
    else:
        print("Failed to get data")
 
def save_to_csv():
    for city, data in weather_data.items():
        dataframe = pd.DataFrame(data)
        dataframe.to_csv(f"{city}_weather_data.csv", index=False)
 
    print("Data is saved to csv")
 
 
try:
    while True:
        for location in locations:
            get_weather(location)
            save_to_csv()
            time.sleep(3)
except KeyboardInterrupt:
    print("Data Collection ended.")
 
    save_to_csv()
    print("Bye")