import subprocess

#for install lib
#subprocess.run(["pip", "install", "pyautogui"])

import random
import time
import pyautogui
import os

# your username
username = os.getlogin()  

#open telegram
subprocess.Popen(f"C:\\Users\\{username}\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")

timestop = 15

time.sleep(120)
pyautogui.moveTo(100, 200)
time.sleep(timestop)

pyautogui.click()
time.sleep(timestop)

pyautogui.moveTo(1250, 700)
time.sleep(timestop)

pyautogui.click()
time.sleep(timestop)

pyautogui.moveTo(200, 650)
time.sleep(timestop)

pyautogui.click()
time.sleep(timestop)

pyautogui.moveTo(200, 580)
time.sleep(timestop)

pyautogui.scroll(int(100))
time.sleep(timestop)

while (True):
	time.sleep((random.random()*1)/8.23)
	pyautogui.click()