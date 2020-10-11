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
number_of_lights = 10

#create the neopixel. auto_write=True avoids having to push changes (at the cost of speed, which probably doesn't matter here)
pixels = neopixel.NeoPixel(board.NEOPIXEL, number_of_lights, brightness = 0.1, auto_write=False)

# sets up the bug holder list, which holds all of the bug objects

bug_holder = []


# sets up the bug class

class Bug:
    def __init__(self, type, reset_time_input, light_number):
        self.type = type
        self.reset_time_input = reset_time_input
        self.light_number = light_number


#functions to turn light on and off
def on(light_num):
    pixels[light_num] = (neo_r, neo_g, neo_b)
    pixels.show()
def off(light_num):
    pixels[light_num] = (0, 0, 0)
    pixels.show()


#functions for the types of fireflies
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


#create all of the light objects by appending a new light object to the list for each neopixel
#the first argument (random.randint(1, 3)) is used to assign a random number which corresponds to one of the ff functions
#if you start adding lots of those it might be worth using a universal variable

for i in range (0, number_of_lights):
    bug_holder.append(Bug(random.randint(1, 3), time.monotonic(), i))


while True:

    #iterates through all of the light objects in the bug_holder list
    #use the series of if statements to match the randomly assigned number to the types of fireflies

    for i in range (0, number_of_lights):
        if bug_holder[i].type == 1:
            bug_holder[i].reset_time_input = brimleyi(bug_holder[i].reset_time_input, i)
        elif bug_holder[i].type == 2:
            bug_holder[i].reset_time_input = macdermotti(bug_holder[i].reset_time_input, i)
        elif bug_holder[i].type == 3:
            bug_holder[i].reset_time_input = carolinus(bug_holder[i].reset_time_input, i)
        #this is just a catchall if there is some sort of error
        else:
            bug_holder[i].reset_time_input = brimleyi(bug_holder[i].reset_time_input, i)
            print("number error")


    #briefly pauses the loop to avoid crashing the USB bus. Also makes it easier to see what is happening.
    time.sleep(0.25)