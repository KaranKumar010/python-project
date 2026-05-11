# Countdown Timer

import time

my_time = int(input("Enter the time in seconds for the countdown:"))

while my_time > 0:
    secods = my_time % 60
    minutes = (my_time // 60) % 60
    hours = (my_time // 3600) % 24
    print(f"{hours:02d}:{minutes:02d}:{secods:02d}")
    time.sleep(1)
    my_time -= 1

print("Time's up!")
