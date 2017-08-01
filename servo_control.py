"""
Control script for sg90 micro servo.

Author: Avery Uslaner
"""
import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Timing setup
delay_time = 3600  # 1 hour


def ready_position(pwm):
    """
    Change the DutyCycle of the PWM object to position the servo at an
    angle so that is not depressing the remote shutter release button.

    :param pwm: Object to control the PWM signal.
    """
    pwm.start(7.8)


def focus_position(pwm):
    """
    Change the DutyCycle of the PWM object to position the servo at an
    angle so that it is half-pressing the remote shutter release button.
    This serves to focus the camera before capturing an image.

    :param pwm: Object to control the PWM signal.
    """
    pwm.start(7.6)


def capture_position(pwm):
    """
    Change the DutyCycle of the PWM object to position the servo at an
    angle so that it is full-pressing the remote shutter release button.
    This activates the camera shutter to capture an image.

    :param pwm: Object to control the PWM signal.
    """
    pwm.start(7.4)


def capture_image(pwm):
    """
    Manipulates servo positions to capture an image and then
    repositions servo to the ready position.

    :param pwm: Object to control the PWM signal.
    """
    focus_position(pwm)
    time.sleep(1)  # Give the camera a second to focus
    capture_position(pwm)  # Take the shot
    time.sleep(0.1)  # Give the servo time to move
    ready_position(pwm)  # Reposition the servo so it is not touching the button anymore


def main():
    pwm = GPIO.PWM(18, 50)  # Set GPIO bin 18 pulse width modulation to 50 Hz
    ready_position(pwm)

    # Initial capture
    capture_image(pwm)

    # Time-lapse loop
    while True:
        time.sleep(delay_time)  # Time between images
        capture_image(pwm)

if __name__ == '__main__':
    main()
