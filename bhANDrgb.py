from machine import Pin, I2C
from utime import sleep
from bh1750 import BH1750

# Define the pins for I2C communication
i2c0_sda = Pin(16)
i2c0_scl = Pin(17)

# Create an I2C object
i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)

# Initialize the BH1750 object
while True:
    try:
        bh1750 = BH1750(0x23, i2c0)
        print("Connected :)")
        break;
    except:
        print("ERROR...")
        #+sleep()

# Read and print the lux values in a loop
while True:
    lux = bh1750.read_lux()
    print(f"Lux: {lux}")
    sleep(1)

