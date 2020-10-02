import pyautogui
import time


msg = input("Enter  message to spam : ")
n = input("How many times to spam ?: ")

print("starting innn.............")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("KA ME HA ME HAAAAAA!!!")

for i in range(0,int(n)):
	pyautogui.typewrite(msg + '\n')