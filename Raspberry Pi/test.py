import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) # red
GPIO.setup(4, GPIO.OUT) # green
GPIO.setup(22, GPIO.OUT) # blue

# init setup
GPIO.output(17, False)
GPIO.output(4, False)
GPIO.output(22, False)

def piano():
    red=0
    green=0
    blue=0
    rgb=0
    rg=0
    gb=0
    rb=0
    try:
        while True:
            asked = raw_input("Red, Green, or Blue?")

            if asked == "r" and red == 0:
                GPIO.output(17, True)
                red = red + 1
                print "red is", red
                print "green is", green
                print "blue is", blue
                
            elif asked == "r" and red == 1:
                GPIO.output(17, False)
                red = red - 1
                print "red is", red
                print "green is", green
                print "blue is", blue

            elif asked == "g" and green == 0:
                GPIO.output(4, True)
                green = green + 1
                print "red is", red
                print "green is", green
                print "blue is", blue
            
            elif asked == "g" and green == 1:
                GPIO.output(4, False)
                green = green - 1
                print "red is", red
                print "green is", green
                print "blue is", blue

            elif asked == "b" and blue == 0:
                GPIO.output(22, True)
                blue = blue + 1
                print "red is", red
                print "green is", green
                print "blue is", blue
                
            elif asked == "b" and blue == 1:
                GPIO.output(22, False)
                blue = blue - 1
                print "red is", red
                print "green is", green
                print "blue is", blue

    except KeyboardInterrupt:
        GPIO.output(17, False)
        GPIO.output(4, False)
        GPIO.output(22, False)
        exit

run = piano()
