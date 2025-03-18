import time
print(time.ctime())
#This function tells you the time on your machine.

print("Start")
time.sleep(10)
print("End")
#We print out start, after the time.sleep function was officially set to 10 seconds, finally printed end to indicate
#that the countdown has ended.

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("Times up!")
#We use a for loop to count down from ten, then printing the i out to activate te code, setting the time.sleep
#function to 1 and finally printing out times up to say that the 10 seconds have finished.