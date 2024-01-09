import pyautogui as pag
import random
import time

while True:
    x = random.randint(100,1800)
    y = random.randint(100,800)
    print(f'\nMoved to: {x,y}')

    speed = round(random.uniform(0.2,0.6),2)
    print(f'\nSpeed: {speed}')

    pag.moveTo(x,y,speed)

    t = random.randint(2,4)
    print(f'\nTime delay: {t}\n')
    time.sleep(t)