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

from adafruit_led_animation.color import RED, BLUE, GREEN, YELLOW, BLACK, PURPLE, ORANGE, PINK, CYAN
import neopixel

ports = {
    1: board.GP17,   # Lantern with 4 LEDs
    2: board.GP19,   # Lantern with 4 LEDs
    3: board.GP21,   # Lantern with 4 LEDs
    4: board.GP22,   # Lantern with 4 LEDs
    5: board.GP26,   # Lantern with 4 LEDs
    6: board.GP28,   # Lantern with 4 LEDs
    7: board.GP15,   # Lantern with 4 LEDs
    8: board.GP13,   # Lantern with 4 LEDs
    9: board.GP16,   # Lantern with 4 LEDs
    10: board.GP18,  # Upper part of title "Homecoming" 43 LEDs
    11: board.GP20,  # Lower part of title "Lantern Festival" 60 LEDs
    12: board.GP27,
    13: board.GP14
}

# ** Change this value to connnect the DIN wire to a different pin on the Pico
pixel_pin = ports[1]



strips = {}

# Initialize the library used to control the neopixel strip
def init_strip(port_num, num_pixels, brightness):
    strips[port_num] = neopixel.NeoPixel(ports[port_num], num_pixels, brightness=brightness, auto_write=False)
    strips[port_num].fill(BLACK)
    strips[port_num].show()

# Initialize bag lights with 4 LEDs each
for port_num in range(1,10):
    init_strip(port_num, 4, .5)
    print("Iniitalized port %d" %(port_num))

#init_strip(10, 10, 1.0) # f or testing, just light 10 pixels
#init_strip(11, 10, 1.0) # for testing, just light 10 pixels

init_strip(10, 43, 1.0)  # The actual strand has 43 pixels
init_strip(11, 60, 1.0)  # The actual strand has 43 pixels

animations = []
colors = [ RED, GREEN, YELLOW, PURPLE, ORANGE, BLACK, PINK, BLUE, CYAN, PURPLE ]
#for key in sorted(strips.keys()):
for key in range(1,10):
    old_colors = colors
    colors = old_colors[1:]
    colors.append(old_colors[0])
    #animations.append(Blink(strips[key], speed=0.25, color=BLUE))
    #animations.append(Comet(strips[key], speed=0.1, color=RED, tail_length=2, bounce= True))
    #animations.append(Sparkle(strips[key], speed=.5, color=YELLOW, num_sparkles=1))
    #animations.append(Pulse(strips[key], speed=.1, color=YELLOW, period=5))
    #animations.append(SparklePulse(strips[key], speed=.1, color=GREEN, period=5))
    animations.append(ColorCycle(strips[key], speed=5, colors=tuple(colors)))
    #animations.append(Solid(strips[key], color=BLACK))


# This is similar to what the EA Makerspace sign does
#animations.append(RainbowChase(strips[10], speed=.05, size=1, spacing=0))
animations.append(RainbowSparkle(strips[10], period=60, speed=1))
animations.append(RainbowSparkle(strips[11], period=60, speed=1))

##############################################################################
# This is the main body of your code
while True:
    [x.animate() for x in animations]
