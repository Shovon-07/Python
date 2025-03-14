import pyautogui
import time

time.sleep(5)
count = 1

while count<=10:
  pyautogui.typewrite("Auto send message " + str(count))
  time.sleep(1)
  pyautogui.press("esc")
  pyautogui.press("enter")
  count+=1
