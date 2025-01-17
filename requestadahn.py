import requests
import datetime
import json


today_date = datetime.datetime.now().date()

print(today_date)

def getInfo(city,country, method=2):
    url = f"https://api.aladhan.com/v1/timingsByCity"
    params = {
        "city": city,
        "country": country,
        "method": method
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        jsoned = json.dumps(data["data"]["timings"], indent=4)
        with open("prayer_times.json", "w") as file:
            file.write(jsoned)    
        print(f"Data saved for {today_date}")    
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None



# Get prayer times for my region (u can change it)
prayer_times = getInfo("Casablanca", "Morocco")
print(prayer_times)
