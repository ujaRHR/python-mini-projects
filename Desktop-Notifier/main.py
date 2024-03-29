import datetime, time, os
from plyer import notification

state = None
try:
    state = "Script is running..."
except:
    print("Please! Check your internet connection")

if (state != None):
    while(True):
        notification.notify(
            title = "Drinking Water Reminder",
            message = "You are not a Cactus! Drink some Water. \rIt's important to stay hydrated.",
            app_icon = f"{os.getcwd()}/icon.ico",
            timeout  = 5
        )
        time.sleep(20) # Reminder after 45 minutes
