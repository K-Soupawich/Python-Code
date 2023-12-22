import time

print("Timer")

minute = int(input("minute : "))
second = int(input("second : "))

if len(str(second)) > 2:
    print("Invalid")
else:
    while minute != -1:
        print("\r", end="")
        print("0"*((len(str(minute)))==1) + str(minute) + ":" + "0"*((len(str(second)))==1) + str(second), end="")
        second -= 1
        time.sleep(1)
        if second == -1:
            second = 59
            minute -= 1
print("\rTimer End")
#print("0"*((len(str(minute)))==1)+str(minute))