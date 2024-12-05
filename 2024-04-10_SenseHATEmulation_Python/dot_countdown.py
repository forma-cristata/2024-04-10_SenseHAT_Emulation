from sense_emu import SenseHat
from time import sleep


sense = SenseHat()

G = [0, 255, 0]
R = [255, 0, 0]
X = [0, 0, 0]

s = 10
timer = []
for i in range(0, 64):
    timer.append(X)
    if i < 10:
        timer[i] = G

for i in range(0, s):
    timer[i] = R
    sense.set_pixels(timer)
    sleep(1)
    
for i in range(0, 10):
    sense.clear()
    sleep(0.1)
    sense.set_pixels(timer)
    sleep(0.1)