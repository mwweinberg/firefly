import board
import digitalio
import time
import neopixel

#create the neopixel. auto_write=True avoids having to push changes (at the cost of speed, which probably doesn't matter here)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.2, auto_write=False)

#instantite the 'zero' counter
action_time_1 = time.monotonic()
action_time_2 = time.monotonic()


def pattern_one(action_time_input, light_number):
    #First LED
    #calculates the difference between when the loop started (action_time_1) and now)
    time_from_action_1 = time.monotonic() - action_time_input

    #using the time from when the loop started to determine if the light should be on or off
    if time_from_action_1 < 9:
        pixels[light_number] = (0, 0, 0)
        pixels.show()
        print(time_from_action_1)
        print("0000000000000000000000")
        action_time =  action_time_input
    if time_from_action_1 > 9 and time_from_action_1 < 20:
        pixels[light_number] = (255, 255, 0)
        pixels.show()
        print(time_from_action_1)
        print("1111111111111111111111")
        action_time =  action_time_input
    if time_from_action_1 > 20:
        pixels[light_number] = (0, 0, 0)
        pixels.show()
        print(time_from_action_1)
        print("2222222222222222222222")
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
        pixels[light_number] = (255, 255, 0)
        pixels.show()

    if 7 < time_from_action_2 <= 9:
        pixels[light_number] = (0, 0, 0)
        pixels.show()

    if 9 < time_from_action_2 <= 12:
        pixels[light_number] = (255, 255, 0)
        pixels.show()

    if 12 < time_from_action_2 <= 15:
        pixels[light_number] = (0, 0, 0)
        pixels.show()

    if 15 < time_from_action_2 <= 22:
        pixels[light_number] = (255, 255, 0)
        pixels.show()

    if time_from_action_2 > 22:
        pixels[light_number] = (0, 0, 0)
        pixels.show()
        action_time = time.monotonic()
    return action_time


while True:

    action_time_1 = pattern_one(action_time_1, 0)
    action_time_2 = pattern_two(action_time_2, 1)




    #briefly pauses the loop to avoid crashing the USB bus. Also makes it easier to see what is happening.
    time.sleep(0.25)