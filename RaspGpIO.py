import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 17 as an output
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        # Turn on the LED
        GPIO.output(17, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 second
        
        # Turn off the LED
        GPIO.output(17, GPIO.LOW)
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    pass

# Clean up the GPIO settings
GPIO.cleanup()
