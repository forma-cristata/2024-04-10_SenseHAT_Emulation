from sense_emu import SenseHat
from time import sleep
import math
sense_emulator = SenseHat()
COLOR_TO_APPROACH = [255, 0, 0]
original_color = [255, 255, 255]
PURPLE = [255, 0, 255]
step = (original_color[1] - COLOR_TO_APPROACH[1]) / 9

def ChangeColorOneNinth():
    original_color[1] = round(original_color[1] - step)
    original_color[2] = round(original_color[2] - step)
i = 9

while(i > -1):
    if i == 0:
        original_color = PURPLE
    sense_emulator.show_letter(str(i), original_color)
    sleep(1)
    ChangeColorOneNinth()
    
    i -= 1
    
