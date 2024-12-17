

import time
import schedule
from mail_auto import send_gmail

email="absproject7@gmail.com"
password="eyeg fciw ojjz nvpx"
receiver="shivaaryal62@gmail.com"

def send_water_reminder():
    subject = "Hello Its time to drink Water"
    body =  "ITs time to drink water and stay hydrated"
    send_gmail(subject, body, email,receiver, password)

#
time_frame=["08:14","08:15","08:16","08:17"]


# Schedule the reminder (choose one of the following to test)

for frame in time_frame:
    schedule.every().day.at(frame).do(send_water_reminder)
# schedule.every().day.at("07:00").do(send_water_reminder_via_local)

# Run the scheduler
print("Starting the hydration reminder app...")
while True:
    schedule.run_pending()
    time.sleep(1)