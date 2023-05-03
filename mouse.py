import pyautogui as mo
import random
import time

while 1 == 1:
  x = random.randint(400, 700)
  y = random.randint(500, 900)
  mo.moveTo(x,y,0.9)
  time.sleep(2)
  
