import RPi.GPIO as GPIO

def callback(channel):
    if GPIO.input(channel):
        relay_on()
        print("motion detected")
    else:
        relay_off()
        print("motion not detected")

def relay_on():
    GPIO.setup(23, GPIO.OUT)

def relay_off():
    GPIO.setup(23, GPIO.IN)

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(23, GPIO.IN)
    GPIO.add_event_detect(18, GPIO.BOTH, callback=callback)
    print("motion listener registered")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
