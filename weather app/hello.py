import requests

API_KEY = "ac61644c2a2902bed0e45aa4e8b8fb54"  
CITY = "delhi"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


url = f"{BASE_URL}?q={CITY}&appid={API_KEY}&units=metric"


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    print(f"The weather in {CITY} is {weather} with a temperature of {temperature}*C.")
else:
    print("Could not retrieve the weather information.")

if (temperature > 0 and temperature < 15):
        print("COLD AND FREEZING")
elif (temperature > 15 and temperature < 25):
        print("WARM AND COLDY")
elif (temperature > 25 and temperature < 35):
        print("HOT")
elif(temperature > 35 and temperature < 45):
       print("VERY HOT")
else:
        print("COULD NOT IDENTIFY")