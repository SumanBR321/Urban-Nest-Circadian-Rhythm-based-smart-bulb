import machine
import neopixel
import time

# Define the number of LEDs
num_leds = 8  # Change this according to your setup

# Define the pin where the LED strip is connected
pin = machine.Pin(0, machine.Pin.OUT)  # Change 0 to the appropriate pin number

# Create a NeoPixel object
np = neopixel.NeoPixel(pin, num_leds)

# Function to set the color of all LEDs
def set_all_leds(color):
    for i in range(num_leds):
        np[i] = color
    np.write()
    
while 0:
    for b in range(255,39,-1):
        set_all_leds((255,170,b));
        time.sleep(.01)
        print(b)
    for b in range(39,256):
        set_all_leds((255,170,b));
        time.sleep(.01)
        print(b)
        
red = [int(i/100) for i in range(23000,25600,12)]
green = [int(i/100) for i in range(23500,14600,-41)]
blue = [i for i in range(255,38,-1)]

while True:
    r,g=0,0
    for i in range(len(blue)):
        if r>=len(red):
            r=len(red)-1
        if g>=len(green):
            g=len(green)-1
        set_all_leds((red[r],green[g],blue[i]))
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
# Main code
if __name__ == "__main__":
    while True:
        # Set all LEDs to red
        set_all_leds((230,235,255))  # (R, G, B)
        time.sleep(1)  # Pause for 1 second

        # Set all LEDs to green
        set_all_leds((243,242,255))
        time.sleep(1)

        # Set all LEDs to blue
        set_all_leds((255,246,237))
        time.sleep(1)
        
        # Set all LEDs to red
        set_all_leds((255,228,206))  # (R, G, B)
        time.sleep(1)  # Pause for 1 second

        # Set all LEDs to green
        set_all_leds((255,224,199))
        time.sleep(1)

        # Set all LEDs to blue
        set_all_leds((255,218,187))
        time.sleep(1)
        
        # Set all LEDs to red
        set_all_leds((255,206,166))  # (R, G, B)
        time.sleep(1)  # Pause for 1 second

        # Set all LEDs to green
        set_all_leds((255,177,110))
        time.sleep(1)

        # Set all LEDs to blue
        set_all_leds((255,167,87))
        time.sleep(1)
        
        # Set all LEDs to blue
        set_all_leds((255,146,39))
        time.sleep(1)
        
