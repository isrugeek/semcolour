from PIL import Image
import sys
import os
from resizeimage import resizeimage

source = 'set to source'
output = 'set to target'
file = 0

def resizer(filename):
    file = 0
    with open(filename, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [256, 256])
            cover.save(output+str(file)+'.jpeg', image.format)
            file+=1
            return cover


resizer(source)

# for filename in os.listdir(source):
#     #output = output+filename
#     filenames = source+filename
#
#     #print (filename)
#     with open(filenames, 'r+b') as f:
#         with Image.open(f) as image:
#             cover = resizeimage.resize_cover(image, [256, 256])
#             cover.save(output+str(file)+'.jpeg', image.format)
#             file+=1
