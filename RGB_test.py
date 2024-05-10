import machine
import neopixel
from machine import Pin, I2C
import uasyncio as asyncio

# Define the pin where the LED strip is connected
pin = machine.Pin(0, machine.Pin.OUT)
# Define the number of LEDs
num_leds = 8

# Create a NeoPixel object
np = neopixel.NeoPixel(pin, num_leds)

# Initialize the BH1750 object
while True:
    r,g,b=input("Enter the R G B: ").split()
    np.fill((int(r),int(g),int(b)))
    np.write()


