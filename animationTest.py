import random
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
value = random.randint(0,2)

R = (238, 37, 10)
O = (238, 141, 10) 
Y = (238, 210, 10)
W = (255, 255, 255)
G =(95, 130, 22)
L = (33, 232, 60 )
B = (0,0,0)
C = (33, 226, 232 )
N = (15, 74, 155 )
try:
    while True:
        if value==0:
            pixels = [
                 B, R, R, B, B, B, O, B,
                 B, B, O, R, R, B, B, B,
                 B, B, R, O, R, R, B, B,
                 B, R, R, O, O, R, R, B,
                 R, R, O, O, O, O, O, R,
                 R, O, O, Y, Y, Y, O, R,
                 R, R, Y, Y, B, Y, R, B,
                 B, R, R, B, B, R, B, B,
            ]
            sense.set_pixels(pixels)
            sleep(0.5)
            pixels = [
                 B, B, B, R, R, B, B, B,
                 B, B, B, R, O, R, B, O,
                 B, B, R, O, O, R, R, B,
                 B, R, R, O, O, O, R, B,
                 R, R, O, O, Y, O, O, R,
                 R, O, O, Y, Y, Y, O, R,
                 R, R, Y, Y, B, Y, R, B,
                 B, R, R, B, B, R, B, B,
            ]
            sense.set_pixels(pixels)
            sleep(0.5)

            sense.clear()
            
        if value == 1:
            sense.show_message("Gas", scroll_speed = 0.1,text_colour=L)
            
        if value == 2:
            pixels = [
                 C, C, W, C, B, B, B, B,
                 N, C, C, C, B, B, N, B,
                 N, N, N, B, B, B, N, B,
                 B, B, B, B, B, C, C, N,
                 B, B, B, B, B, C, C, W,
                 B, B, B, B, N, C, C, W,
                 B, B, B, B, N, N, C, C,
                 B, B, B, B, B, N, N, N,
            ]
            sense.set_pixels(pixels)
            sleep(0.1)
            pixels = [
                 C, C, W, B, B, B, B, B,
                 C, C, W, C, B, B, B, B,
                 N, C, C, C, B, B, N, B,
                 N, N, N, B, B, B, N, B,
                 B, B, B, B, B, C, C, N,
                 B, B, B, B, B, C, C, W,
                 B, B, B, B, N, C, C, W,
                 B, B, B, B, N, N, C, C,
            ]
            sense.set_pixels(pixels)
            sleep(0.1)
            pixels = [
                 C, C, N, B, B, B, B, B,
                 C, C, W, B, B, B, B, B,
                 C, C, W, C, B, B, B, B,
                 N, C, C, C, B, B, N, B,
                 N, N, N, B, B, B, N, B,
                 B, B, B, B, B, C, C, N,
                 B, B, B, B, B, C, C, W,
                 B, B, B, B, N, C, C, W,
            ]
            sense.set_pixels(pixels)
            sleep(0.1)
            pixels = [
                 B, N, B, B, B, N, N, N,
                 C, C, N, B, B, B, B, B,
                 C, C, W, B, B, B, B, B,
                 C, C, W, C, B, B, B, B,
                 N, C, C, C, B, B, N, B,
                 N, N, N, B, B, B, N, B,
                 B, B, B, B, B, C, C, N,
                 B, B, B, B, B, C, C, W,
            ]
            sense.set_pixels(pixels)
            sleep(0.1)
            pixels = [
                 B, N, B, B, N, N, C, C,
                 B, N, B, B, B, N, N, N,
                 C, C, N, B, B, B, B, B,
                 C, C, W, B, B, B, B, B,
                 C, C, W, C, B, B, B, B,
                 N, C, C, C, B, B, N, B,
                 N, N, N, B, B, B, N, B,
                 B, B, B, B, B, C, C, N,
            ]
            sense.set_pixels(pixels)
            sleep(0.1)
            pixels = [
                 B, B, B, B, N, C, C, W,
                 B, N, B, B, N, N, C, C,
                 B, N, B, B, B, N, N, N,
                 C, C, N, B, B, B, B, B,
                 C, C, W, B, B, B, B, B,
                 C, C, W, C, B, B, B, B,
                 N, C, C, C, B, B, N, B,
                 N, N, N, B, B, B, N, B,
            ]
            sense.set_pixels(pixels)
            sleep(0.1)
            pixels = [
                 B, B, B, B, B, C, C, W,
                 B, B, B, B, N, C, C, W,
                 B, N, B, B, N, N, C, C,
                 B, N, B, B, B, N, N, N,
                 C, C, N, B, B, B, B, B,
                 C, C, W, B, B, B, B, B,
                 C, C, W, C, B, B, B, B,
                 N, C, C, C, B, B, N, B,
            ]
            sense.set_pixels(pixels)
            sleep(0.1)
            pixels = [
                 B, B, B, B, B, C, C, N,
                 B, B, B, B, B, C, C, W,
                 B, B, B, B, N, C, C, W,
                 B, N, B, B, N, N, C, C,
                 B, N, B, B, B, N, N, N,
                 C, C, N, B, B, B, B, B,
                 C, C, W, B, B, B, B, B,
                 C, C, W, C, B, B, B, B,
            ]
            sense.set_pixels(pixels)
            sleep(0.1)
            pixels = [
                 N, N, N, B, B, B, N, B,
                 B, B, B, B, B, C, C, N,
                 B, B, B, B, B, C, C, W,
                 B, B, B, B, N, C, C, W,
                 B, N, B, B, N, N, C, C,
                 B, N, B, B, B, N, N, N,
                 C, C, N, B, B, B, B, B,
                 C, C, W, B, B, B, B, B,
            ]
            sense.set_pixels(pixels)
            sleep(0.1)
            pixels = [
                 N, C, C, C, B, B, N, B,
                 N, N, N, B, B, B, N, B,
                 B, B, B, B, B, C, C, N,
                 B, B, B, B, B, C, C, W,
                 B, B, B, B, N, C, C, W,
                 B, N, B, B, N, N, C, C,
                 B, N, B, B, B, N, N, N,
                 C, C, N, B, B, B, B, B,
            ]
            sense.set_pixels(pixels)
            sleep(0.1)
            sense.clear()
except KeyboardInterrupt:
    sense.clear()
    print("Bye bye")