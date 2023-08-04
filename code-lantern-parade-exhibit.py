# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.solid import Solid

from adafruit_led_animation.color import RED, BLUE, GREEN, YELLOW, BLACK, PURPLE
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



strips = {}

# Initialize the library used to control the neopixel strip
def init_strip(port_num, num_pixels):
    strips[port_num] = neopixel.NeoPixel(ports[port_num], num_pixels, brightness=1, auto_write=False)
    strips[port_num].fill(BLACK)
    strips[port_num].show()

# Initialize bag lights
for port_num in range(1,9):
    init_strip(port_num, 4)

init_strip(10, 10)
init_strip(11, 10)

animations = []
#for key in sorted(strips.keys()):
for key in range(1,9):
    #animations.append(Blink(strips[key], speed=0.25, color=BLUE))
    #animations.append(Comet(strips[key], speed=0.1, color=RED, tail_length=2, bounce= True))
    #animations.append(Sparkle(strips[key], speed=.5, color=YELLOW, num_sparkles=1))
    #animations.append(Pulse(strips[key], speed=.1, color=YELLOW, period=5))
    #animations.append(SparklePulse(strips[key], speed=.1, color=GREEN, period=5))
    #animations.append(ColorCycle(strips[key], speed=.1, colors=(RED, GREEN, BLUE, YELLOW, PURPLE)))
    animations.append(Solid(strips[key], color=BLACK))

# This is similar to what the EA Makerspace sign does
#animations.append(RainbowChase(strips[10], speed=.05, size=1, spacing=0))
animations.append(RainbowSparkle(strips[10], period=60, speed=.25))
animations.append(RainbowSparkle(strips[11], period=60, speed=.25))

##############################################################################
# This is the main body of your code
while True:
    [x.animate() for x in animations]
