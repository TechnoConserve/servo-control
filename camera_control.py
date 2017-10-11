#!/home/pi/venv/servo_env/bin/python

from subprocess import call
import os
import time


def capture_image(count, wait=900):
    """
    By default, takes an image every 15 minutes.

    Alternatively, you could use the --interval flag
    of gphoto2 to control the interval.
    """
    print('Capturing Image!')
    call(['gphoto2', '--capture-image-and-download', '--filename', '{}.jpeg'.format(count)])
    print('Waiting {} seconds...'.format(wait))
    time.sleep(wait)


def get_count():
    """
    Finds and returns the number for the next image filename based
    on existing files.

    The image directory here may need to be modified if you would
    prefer to save images elsewhere.
    """
    count = 0
    # Iterate through the list of files
    for file in os.listdir('/home/pi/images'):
        # Get the string representation of the number in the filename
        num_str = file.split('.')[0]
        # Convert to an actual number
        num = int(num_str)
        # If the current filename is a larger number than the current
        # count variable, assign that value to the count variable
        if num > count:
            count = num

    # Add one to the count variable so the next filename doesn't
    # Overwrite an existing file.
    count += 1
    return count


def main():
    count = get_count()
    while True:
        capture_image(count)
        count += 1


if __name__ == "__main__":
    main()
