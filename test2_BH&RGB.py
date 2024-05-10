import machine
import neopixel
from machine import Pin, I2C
from utime import sleep
from bh1750 import BH1750
import uasyncio as asyncio

# Define the pins for I2C communication
i2c0_sda = Pin(16)
i2c0_scl = Pin(17)
# Define the pin where the LED strip is connected
pin = machine.Pin(0, machine.Pin.OUT)
# Define the number of LEDs
num_leds = 8

# Create an I2C object
i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)
# Create a NeoPixel object
np = neopixel.NeoPixel(pin, num_leds)

# Initialize the BH1750 object
bh1750 = BH1750(0x23, i2c0)

# Function to set the color and brightness of all LEDs
async def set_all_leds(color, brightness):
    r, g, b = color
    r = int(r * brightness)
    g = int(g * brightness)
    b = int(b * brightness)
    for i in range(num_leds):
        np[i] = (r, g, b)
    np.write()

# Coroutine to control the RGB LED
async def rgb_led():
    red = [int(i / 100) for i in range(23000, 25600, 12)]
    green = [int(i / 100) for i in range(23500, 14600, -41)]
    blue = [i for i in range(255, 38, -1)]
    brightness = 1
    while True:
        r, g = 0, 0
        brightness /= 2
        for i in range(len(blue)):
            if r >= len(red):
                r = len(red) - 1
            if g >= len(green):
                g = len(green) - 1
            await set_all_leds((red[r], green[g], blue[i]), brightness)
            await asyncio.sleep(0.1)
            print(red[r], green[g], blue[i])
            r += 1
            g += 1

# Coroutine to read and print lux values from BH1750 sensor
async def read_bh1750():
    while True:
        lux = bh1750.read_lux()
        print(f"Lux: {lux}")
        await asyncio.sleep(1)

# Run both coroutines concurrently
async def main():
    await asyncio.gather(
        rgb_led(),
        read_bh1750()
    )

# Run the event loop
asyncio.run(main())
