"""
Script that renames image files based on the DateTimeOriginal key of their
EXIF metadata.

Author: Avery Uslaner
"""
from datetime import datetime
import os
import PIL.Image
import PIL.ExifTags

# The directory where our images are located
PHOTO_DIRECTORY = '/home/ave/Documents/Work/CTS/timelapse/Images/'
# The directory we want to save our renamed images
PROCESSED_DIRECTORY = 'processed/'

for file in os.listdir(PHOTO_DIRECTORY):
    # Make sure to skip directories-- we are only interested in image files
    path = os.path.join(PHOTO_DIRECTORY, file)
    if os.path.isdir(path):
        continue
    print('Processing ', file)
    img = PIL.Image.open(PHOTO_DIRECTORY + file)
    exif_date = {
        PIL.ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in PIL.ExifTags.TAGS
        and PIL.ExifTags.TAGS[k] == 'DateTimeOriginal'
    }
    image_time = datetime.strptime(exif_date['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
    # Name the new file using the timestamp from the EXIF data
    new_filename = image_time.strftime('%m-%d-%Y_%H-%M') + '.jpeg'
    img.save(PHOTO_DIRECTORY + PROCESSED_DIRECTORY + new_filename, 'JPEG')
    print('Saveing as {} to {}.'.format(new_filename, PHOTO_DIRECTORY + PROCESSED_DIRECTORY))
