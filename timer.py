import time

my_time = int(input("Enter the timer in secs"))

for x in range(my_time, 0 , -1):
    secs = x % 60
    mins = int(x/60) % 60
    hrs = int(x/3500)%60
    print(f"{hrs:02}:{mins:02}:{secs:02}")
    time.sleep(1)

print("Times up!!")
