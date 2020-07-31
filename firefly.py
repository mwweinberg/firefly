#https://www.nps.gov/grsm/learn/nature/firefly-flash-patterns.htm

import board
import digitalio
import time
import neopixel
import random

#create the neopixel. auto_write=True avoids having to push changes (at the cost of speed, which probably doesn't matter here)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.2, auto_write=False)

#variables to hold the color that hte LED will blink
neo_r = 255
neo_g = 255
neo_b = 0


#instantite the 'zero' counter
#right now you need on of these (reset_time_x) for each light
action_time_1 = time.monotonic()
action_time_2 = time.monotonic()

reset_time_2 = time.monotonic()
reset_time_3 = time.monotonic()
reset_time_4 = time.monotonic()


def pattern_one(action_time_input, light_number):
    #First LED
    #calculates the difference between when the loop started (action_time_1) and now)
    time_from_action_1 = time.monotonic() - action_time_input

    #using the time from when the loop started to determine if the light should be on or off
    if time_from_action_1 < 9:
        pixels[light_number] = (0, 0, 0)
        pixels.show()
        action_time =  action_time_input
    if time_from_action_1 > 9 and time_from_action_1 < 20:
        pixels[light_number] = (neo_r, neo_g, neo_b)
        pixels.show()
        action_time =  action_time_input
    if time_from_action_1 > 20:
        pixels[light_number] = (0, 0, 0)
        pixels.show()
        #this is the end of the cycle so the time counting is reset
        action_time = time.monotonic()
    return action_time

def pattern_two(action_time_input, light_number):
    # Second LED
    time_from_action_2 = time.monotonic() - action_time_input
    action_time =  action_time_input
    if time_from_action_2 < 4:
        pixels[light_number] = (0, 0, 0)
        pixels.show()

    if 4 <= time_from_action_2 <= 6:
        pixels[light_number] = (neo_r, neo_g, neo_b)
        pixels.show()

    if 7 < time_from_action_2 <= 9:
        pixels[light_number] = (0, 0, 0)
        pixels.show()

    if 9 < time_from_action_2 <= 12:
        pixels[light_number] = (neo_r, neo_g, neo_b)
        pixels.show()

    if 12 < time_from_action_2 <= 15:
        pixels[light_number] = (0, 0, 0)
        pixels.show()

    if 15 < time_from_action_2 <= 22:
        pixels[light_number] = (neo_r, neo_g, neo_b)
        pixels.show()

    if time_from_action_2 > 22:
        pixels[light_number] = (0, 0, 0)
        pixels.show()
        action_time = time.monotonic()
    return action_time

def brimleyi(reset_time_input, light_number):
    #calculates how much time has passed since the new zero
    time_from_zero = time.monotonic() - reset_time_input
    # creates the carry over reset_time variable so that it can be returned even if it is not updated in the last if statement
    reset_time = reset_time_input

    # on flash
    if 5 <= time_from_zero <= 5.5:
        pixels[light_number] = (neo_r, neo_g, neo_b)
        pixels.show()
        print("b1")
        print(time_from_zero)
    elif 15 <= time_from_zero <= 15.5:
        pixels[light_number] = (neo_r, neo_g, neo_b)
        pixels.show()
        print("b2")
        print(time_from_zero)

    # reset (includes 10 seconds after second flash - 5 on the back end and 5 on the front end)
    elif time_from_zero > 20:
        pixels[light_number] = (0, 0, 0)
        pixels.show()
        reset_time = time.monotonic() + random.uniform(-3, 3)

    # all of the off times
    else:
        pixels[light_number] = (0, 0, 0)
        pixels.show()
        print("b000000")
        print(time_from_zero)

    return reset_time

def macdermotti (reset_time_input, light_number):
    #calculates how much time has passed since the new zero
    time_from_zero = time.monotonic() - reset_time_input
    # creates the carry over reset_time variable so that it can be returned even if it is not updated in the last if statement
    reset_time = reset_time_input

    # on flash
    if 3 <= time_from_zero <= 3.5:
        pixels[light_number] = (neo_r, neo_g, neo_b)
        pixels.show()
    elif 5 <= time_from_zero <= 5.5:
        pixels[light_number] = (neo_r, neo_g, neo_b)
        pixels.show()
    elif 10 <= time_from_zero <= 10.5:
        pixels[light_number] = (neo_r, neo_g, neo_b)
        pixels.show()
    elif 12 <= time_from_zero <= 12.5:
        pixels[light_number] = (neo_r, neo_g, neo_b)
        pixels.show()

    elif time_from_zero > 14.5:
        pixels[light_number] = (0, 0, 0)
        pixels.show()
        reset_time = time.monotonic() + random.uniform(-3, 3)

    else:
        pixels[light_number] = (0, 0, 0)
        pixels.show()

    return reset_time

while True:

    action_time_1 = pattern_one(action_time_1, 0)
    action_time_2 = pattern_two(action_time_2, 1)

    reset_time_2 = brimleyi(reset_time_2, 2)
    reset_time_3 = brimleyi(reset_time_3, 3)
    reset_time_4 = macdermotti(reset_time_4, 4)





    #briefly pauses the loop to avoid crashing the USB bus. Also makes it easier to see what is happening.
    time.sleep(0.25)