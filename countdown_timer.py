# Project : 5 Count Down timer Program 

import time  # ✅ Added import 

my_time = int(input("Enter the number of seconds to pause: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x // 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's UP")
 

