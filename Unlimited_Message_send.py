import pyautogui
import time

time.sleep(2)
count = 1

while count<=10 :
  pyautogui.typewrite("Auto send message " + str(count))
  time.sleep(2)
  pyautogui.press("enter")
  count+=1