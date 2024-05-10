import machine
import neopixel
from machine import Pin, I2C
from bh1750 import BH1750
import uasyncio as asyncio

# Define the pins for I2C communication BH1750
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
        brightness = 1-(min(lux,500)) / 500 # Limit brightness to a maximum value (0 to 1)+
        # Set NeoPixel colors
        np.fill((int(255 * brightness), int(167 * brightness), int(87 * brightness)))
        np.write()
        print(f"Brightness: {brightness*100:.2f}%, LUX: {lux}")
        
        await asyncio.sleep(1)

# Run the event loop with the RGB LED intensity coroutine
async def main():
    await rgb_led_intensity()

# Run the event loop
asyncio.run(main())

