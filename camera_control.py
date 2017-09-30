#!/home/pi/venv/servo_env/bin/python

from subprocess import call
import time


def capture_image(wait=1800):
    """
    By default, takes an image every 30 minutes.

    Alternatively, you could use the --interval flag
    of gphoto2 to control the interval.
    """
    print('Capturing Image!')
    call(['gphoto2', '--capture-image-and-download', '--filename %:'])
    print('Waiting {} seconds...'.format(wait))
    time.sleep(wait)


def main():
    while True:
        capture_image()


if __name__ == "__main__":
    main()
