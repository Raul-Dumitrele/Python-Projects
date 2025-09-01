# pip install psutil
import psutil
# pip install py-notifier
# pip install win10toast
from pynotifier import Notification


battery=psutil.sensors_battery()
plugged=battery.power_plugged
percent=battery.percent

if percent<=30 and plugged!=True:
    Notification(
        title="Low Battery",
        description=f"{percent}% Battery remaining!!",
        duration=5,  # secunde
    ).send()
    
