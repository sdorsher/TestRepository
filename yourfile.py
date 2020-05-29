from datetime import datetime
import time
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print("Still waiting for you...")
time.sleep(30)
current_time = now.strftime("%H:%M:%S")
print("Current Time=", current_time)
print("These stories don't mean anything without someone to tell them to")
