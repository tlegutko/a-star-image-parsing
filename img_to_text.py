from PIL import Image
import sys
import re
import os

pixel_to_symbol = {
        (255, 255, 255): '0 ', # white -> nothing
        (0, 0, 0): '1 ', # black -> border / obstacle
        (0, 255, 0): '2 ', # green -> start
        (255, 0, 0): '3 ', # red -> end
}

def parse_file(file_name):
    image = Image.open('img_in/{0}'.format(file_name))
    output = re.sub(r'(.*)\.bmp', r'text_in/\1.in', file_name)
    f = open(output, 'w')
    f.write(' '.join(map(str, image.size)))
    f.write('\n')
    for row in range(image.height):
        for col in range(image.width):
            f.write(pixel_to_symbol[(image.getpixel((col, row)))])
        f.write('\n')

for root, dirs, files in os.walk("img_in"):
    for file in files:
        if file.endswith('.bmp'):
            parse_file(file)

