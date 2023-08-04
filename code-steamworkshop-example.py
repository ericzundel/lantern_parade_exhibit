# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel

ports = {
    1: board.GP17,
    2: board.GP19,
    3: board.GP21,
    4: board.GP22,
    5: board.GP26,
    6: board.GP28,
    7: board.GP15,
    8: board.GP13,
    9: board.GP16,
    10: board.GP18,
    11: board.GP20,
    12: board.GP27,
    13: board.GP14
}

# ** Change this value to connnect the DIN wire to a different pin on the Pico
pixel_pin = ports[1]

# ** Change this number to be the number of LEDs on your strips
num_pixels = 10

strips = {}
# This line initializes the library used to control the neopixel strip
for port_num in sorted(ports.keys()):
    strips[port_num] = neopixel.NeoPixel(ports[port_num], num_pixels, brightness=1, auto_write=False)

pixels = strips[4]

# Different colors are made by mixing different amounts of
# Red, Green and Blue light.  The color wheel for light
# is different from mixing paint!
#
# Here are some RGB values for some common colors.
# 0 == LED off and 255 == full brightness
RED    = (255,   0,   0) # 100% red,   0% green, 0% blue
GREEN  = (  0, 255,   0) #   0% red, 100% green, 0% blue
BLUE   = (  0,   0, 255) # 100% blue
CYAN   = (  0, 255, 255) #   0% red, 100% green, 100% blue
YELLOW = (255, 150,   0) # 100% red,  55% green, 0% blue
WHITE  = (100, 100, 100) # 100% of all colors
BLACK  = (  0,   0,   0) # 0% of all colors (turns the LED off)

# ** Can you figure out the values for these colors?
#LIGHTBLUE = (?, ?, ?)
#LIGHTPINK = (?, ?, ?)
#ORANGE = (?, ?, ?)
#CYAN = (?, ?, ?)
#PURPLE = (?, ?, ?)
#MAGENTA = (?, ?, ?)

# ** Make your own colors and see what happens!
#MYCOLOR1 RGB(?, ?, ?)
#MYCOLOR2 RGB(?, ?, ?)
#MYCOLOR3 RGB(?, ?, ?)
#MYCOLOR4 RGB(?, ?, ?)

# *****************************************************************************
# ** These are the functions used to make different patterns.
# ** Skip down to "while True:" below to start making your changes to the code
# *****************************************************************************
def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

def rainbow(wait):
  for count in range(256):
    for pixel_num in range(len(pixels)):
        pixels[pixel_num] = colorwheel((pixel_num + count) % 255)
    pixels.show()
    time.sleep(wait);

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index % 255)
        pixels.show()
        time.sleep(wait)

# theater_chase(color, wait)
# Theatre-style crawling lights.
#  color - The color to use for the LEDs
#  wait - The number of seconds to wait between turning the LEDs on and off.
def theater_chase(color, wait):
  for j in range(10): #do 10 cycles of chasing
    for q in range(3):
      for i in range(0, len(pixels)-1, 3):
        pixels[i+q] = color # turn every third pixel on
      pixels.show()
      time.sleep(wait);

      for i in range(0, len(pixels)-1, 3):
        pixels[i+q] = BLACK # turn every third pixel off

# theater_chase2(color, wait)
# Theatre-style crawling lights with 2 colors.
#  color1 - A color to use for the LEDs
#  color2 - A second color to follow the first
#  wait - The number of seconds to wait between turning the LEDs on and off.
def theater_chase2(color1, color2, wait):
  for j in range(10): #do 10 cycles of chasing
    for q in range(3):
      for i in range(0, len(pixels)-1, 3):
        pixels[i+q] = color1
        pixels[i+q+1] = color2
      pixels.show()
      time.sleep(wait);

      for i in range(0, len(pixels)-1, 3):
        pixels[i+q] = BLACK # turn every third pixel off

# Theatre-style crawling lights with 3 colors.
#  color1 - A color to use for the LEDs
#  color2 - A second color
#  color3 - A third color
#  wait - The number of seconds to wait between turning the LEDs on and off.
def theater_chase3(color1, color2, color3, wait):
  for j in range(10): #do 10 cycles of chasing
    for q in range(4):
      for i in range(0, len(pixels)-3, 4):
        pixels[i+q] = color1
        pixels[i+q+1] = color2
        pixels[i+q+2] = color3
      pixels.show()
      time.sleep(wait);

      for i in range(0, len(pixels)-3, 4):
        pixels[i+q] = BLACK # turn every third pixel off

# Theatre-style crawling lights with rainbow colors.
#  color - The color to use for the LEDs
#  wait - The number of seconds to wait between turning the LEDs on and off.
def theater_chase_rainbow(wait):
  for j in range(0, 255, 5): #
    for q in range(3):
      for i in range(0, len(pixels)-1, 3):
        pixels[i+q] = colorwheel((i + j) % 255) # turn every third pixel on
      pixels.show()
      time.sleep(wait);

      for i in range(0, len(pixels)-1, 3):
        pixels[i+q] = BLACK # turn every third pixel off

##############################################################################
# This is the main body of your code
while True:

    # Clear out the pixel strip
    pixels.fill(BLACK)

    # ** You can make changes below here

    # print() shows a message in the Serial Monitor.
    # Open it using the "Serial" icon at the top of the Mu Editor
    print("Showing colors");

    # Setting pixel[N] to a color sets one pixel at position N to a specific color
    # Note that the first pixel starts at zero!

    # Set the first 5 pixels to a specific color
    pixels[0] = RED
    pixels[1] = BLUE
    pixels[2] = GREEN
    pixels[6] = RED
    pixels[7] = RED
    pixels[8] = RED
    pixels[9] = RED

    # pixels.show() must be called for any changes with SET() to take effect.
    pixels.show()

    # time.sleep() pauses the program for the specified number of seconds.
    # You can use a decimal to pause for less than a second, e.g. time.sleep(.5)
    time.sleep(2)

    # pixels.fill() sets every LED to the same color
    print ("Turning off all LEDs on the strip");
    pixels.fill(BLACK)
    pixels.show()
    time.sleep(2)

    #print("Seting the strip to a solid color")
    #pixels.fill(RED)
    #pixels.show()
    #time.sleep(2)

    print("color_chase(BLUE): moves red across the strip")
    color_chase(BLUE, 0.1)  # Increase the number to slow down the color chase

    #print("theater_chase(): make lights run up the strip")
    #theater_chase(RED, .1)

    #print("theater_chase2(): make lights run up the strip")
    #theater_chase2(CYAN, YELLOW, .1)

    #print("theater_chase3(): make lights run up the strip")
    #theater_chase3(RED, WHITE, BLUE, .1)

    #print("theater_chase_rainbow(): make lights run up the strip")
    #theater_chase_rainbow(.05)

    #print("rainbow(): LEDs cycle through the colors one at a time.")
    #rainbow(.02)

    #print("rainbow_cycle(): fade different colors with 20ms between colors")
    #rainbow_cycle(.02)
