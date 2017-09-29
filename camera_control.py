from subprocess import call


def capture_image():
    call(['gphoto2', '--capture-image-and-download'])
