from subprocess import call
import time


def capture_image(wait=1800):
    """
    By default, takes an image every 30 minutes.

    Alternatively, you could use the --interval flag
    of gphoto2 to control the interval.
    """
    time.sleep(wait)
    call(['gphoto2', '--capture-image-and-download'])


def main():
    while True:
        capture_image()