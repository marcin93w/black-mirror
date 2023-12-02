import RPi.GPIO as GPIO

def callback(channel):
    if GPIO.input(channel):
        print("GPIO pin", channel, "is HIGH")
    else:
        print("GPIO pin", channel, "is LOW")

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(1, GPIO.BOTH, callback=callback)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
