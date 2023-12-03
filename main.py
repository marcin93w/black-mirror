import RPi.GPIO as GPIO

def callback(channel):
    if GPIO.input(channel):
        print("GPIO pin", channel, "is HIGH")
    else:
        print("GPIO pin", channel, "is LOW")

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(18, GPIO.BOTH, callback=callback)
    print("motion listener registered")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
