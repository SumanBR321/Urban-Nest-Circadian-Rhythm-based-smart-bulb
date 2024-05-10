import machine
import neopixel
import time

# Define the number of LEDs
num_leds = 8

# Define the pin where the LED strip is connected
pin = machine.Pin(0, machine.Pin.OUT)  

# Create a NeoPixel object
np = neopixel.NeoPixel(pin, num_leds)

# Function to set the color and brightness of all LEDs
def set_all_leds(color,brightness):
    r,g,b = color
    r = int(r * brightness)
    g = int(g * brightness)
    b = int(b * brightness)
    for i in range(num_leds):
        np[i] = (r,g,b)
    np.write()

red = [int(i/100) for i in range(23000,25600,12)]
green = [int(i/100) for i in range(23500,14600,-41)]
blue = [i for i in range(255,38,-1)]
brightness = 1
while True:
    r,g=0,0
    brightness/=2
    for i in range(len(blue)):
        if r>=len(red):
            r=len(red)-1
        if g>=len(green):
            g=len(green)-1
        set_all_leds((red[r],green[g],blue[i]),brightness)
        time.sleep(0.1)
        print(red[r],green[g],blue[i])
        r+=1
        g+=1
        
while 0:
    for b in range(255,39,-1):
        set_all_leds((255,170,b));
        time.sleep(.01)
        print(b)
    for b in range(39,256):
        set_all_leds((255,170,b));
        time.sleep(.01)
        print(b)
