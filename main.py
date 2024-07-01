import pyautogui as pa

import time

# NOTE : This program may not be work in your as pc dimension would be different
# print(pa.size()) :- use this to know your p dimension

# print(pa.mouseInfo()):- use this to know coordinates

# my browser coordinates
pa.moveTo(x=996, y=1050)
pa.click()
time.sleep(2)

# this will start the game
pa.moveTo(939, 590)
pa.click()

# detect the obstacle and jump dino
while True:
    if pa.pixelMatchesColor(444, 668, (83, 83, 83)):
        # print(pix)
        pa.press('space')
