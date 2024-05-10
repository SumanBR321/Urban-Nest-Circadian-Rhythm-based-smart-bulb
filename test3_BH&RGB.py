
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
# Define the the Intensity you want
intensity = 1000
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
        lux = bh1750.read_lux()
        
        brightness = (500-lux)/1000
        brightness = min(brightness,1)
        #print(brightness)
        for i in range(len(blue)):
            lux = bh1750.read_lux()
            brightness = (1000-lux)/1000
            brightness = min(brightness,1)
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



'''
import machine
import neopixel
from machine import Pin, I2C
from bh1750 import BH1750
import uasyncio as asyncio

# Define the pins for I2C 0communication BH1750
i2c0_sda = Pin(16)
i2c0_scl = Pin(17)
# Define the pin where the LED strip is connected
pin = machine.Pin(0, machine.Pin.OUT)
# Define the number of LEDs
num_leds = 8

# Create a NeoPixel object
np = neopixel.NeoPixel(pin, num_leds)

# Initialize the BH1750 object
i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)
bh1750 = BH1750(0x23, i2c0)

# Coroutine to control the RGB LED intensity based on lux value
async def rgb_led_intensity():
    while True:
        lux = bh1750.read_lux()
        # Map lux value to LED brightness (adjust the scaling factor as needed)
        brightness = 1-(min(lux,500)) / 500  # Adjust this factor as needed
        # Limit brightness to a maximum value (0 to 1)
        brightness = min(brightness, 1)
        # Set NeoPixel colors
        np.fill((int(255 * brightness), int(255 * brightness), int(255 * brightness)))
        np.write()
        print("Lux:", lux, "Brightness:", brightness)
        await asyncio.sleep(1)

# Run the event loop with the RGB LED intensity coroutine
async def main():
    await rgb_led_intensity()

# Run the event loop
asyncio.run(main())
'''

