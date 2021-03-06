#https://www.nps.gov/grsm/learn/nature/firefly-flash-patterns.htm

import board
import digitalio
import time
import neopixel
import random



#variables to hold the color that the LED will blink
neo_r = 255
neo_g = 255
neo_b = 0

# variable to hold the number of neopixels
number_of_lights = 7

#create the neopixel. auto_write=True avoids having to push changes (at the cost of speed, which probably doesn't matter here)
pixels = neopixel.NeoPixel(board.NEOPIXEL, number_of_lights, brightness = 0.2, auto_write=False)

# automatically spins up the seed reset times for each light
reset_time_dict = {}

# sets the seeds to zero
for i in range(0, number_of_lights):
    var_name = 'resetTime' + str(i)
    reset_time_dict[var_name] = time.monotonic()


print(reset_time_dict)

def on(light_num):
    pixels[light_num] = (neo_r, neo_g, neo_b)
    pixels.show()
def off(light_num):
    pixels[light_num] = (0, 0, 0)
    pixels.show()

def brimleyi(reset_time_input, light_number):
    #calculates how much time has passed since the new zero
    time_from_zero = time.monotonic() - reset_time_input
    # creates the carry over reset_time variable so that it can be returned even if it is not updated in the last if statement
    reset_time = reset_time_input

    # on flash
    if 5 <= time_from_zero <= 5.5:
        on(light_number)
    elif 15 <= time_from_zero <= 15.5:
        on(light_number)

    # reset (includes 10 seconds after second flash - 5 on the back end and 5 on the front end)
    elif time_from_zero > 20:
        off(light_number)
        reset_time = time.monotonic() + random.uniform(-3, 3)

    # all of the off times
    else:
        off(light_number)

    return reset_time

def macdermotti (reset_time_input, light_number):
    #calculates how much time has passed since the new zero
    time_from_zero = time.monotonic() - reset_time_input
    # creates the carry over reset_time variable so that it can be returned even if it is not updated in the last if statement
    reset_time = reset_time_input

    # on flash
    if 3 <= time_from_zero <= 3.5:
        on(light_number)
    elif 5 <= time_from_zero <= 5.5:
        on(light_number)
    elif 10 <= time_from_zero <= 10.5:
        on(light_number)
    elif 12 <= time_from_zero <= 12.5:
        on(light_number)

    elif time_from_zero > 14.5:
        off(light_number)
        reset_time = time.monotonic() + random.uniform(-3, 3)

    else:
        off(light_number)

    return reset_time

def carolinus(reset_time_input, light_number):
    time_from_zero = time.monotonic() - reset_time_input
    # creates the carry over reset_time variable so that it can be returned even if it is not updated in the last if statement
    reset_time = reset_time_input

    if 0 <= time_from_zero <= 0.5:
        on(light_number)
    elif 1 <= time_from_zero <= 1.5:
        on(light_number)
    elif 2 <= time_from_zero <= 2.5:
        on(light_number)
    elif 3 <= time_from_zero <= 3.5:
        on(light_number)
    elif 4 <= time_from_zero <= 4.5:
        on(light_number)
    elif 5 <= time_from_zero <= 5.5:
        on(light_number)
    elif 6 <= time_from_zero <= 6.5:
        on(light_number)

    elif time_from_zero >= 15:
        off(light_number)
        reset_time = time.monotonic()

    else:
        off(light_number)

    return reset_time


while True:

    reset_time_dict["resetTime2"] = brimleyi(reset_time_dict["resetTime2"], 2)
    reset_time_dict["resetTime3"] = brimleyi(reset_time_dict["resetTime3"], 3)
    reset_time_dict["resetTime4"] = macdermotti(reset_time_dict["resetTime4"], 4)
    reset_time_dict["resetTime5"] = carolinus(reset_time_dict["resetTime5"], 5)
    reset_time_dict["resetTime6"] = carolinus(reset_time_dict["resetTime6"], 6)





    #briefly pauses the loop to avoid crashing the USB bus. Also makes it easier to see what is happening.
    time.sleep(0.25)