import datetime
import json
import time
import subprocess

with open("prayer_times.json", "r") as file:
    data = json.load(file)

def notifier():
    while True:
        time_now = datetime.datetime.now().time()
        formatted_time = time_now.strftime("%H:%M")
    

        # loop

        for key, value in data.items():
            if formatted_time == value:
                print(f"It's {key} time")
                formatted_string = f"It's {key} time"
                # Notification Send
                subprocess.run(["notify-send" , formatted_string])

                break
        else:
            print("No prayer time yet")

        time.sleep(50)

notifier()
