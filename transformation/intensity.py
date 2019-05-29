from PIL import Image
import math

def logarithmic(img_input, const):
    """ """
    print(f'\ttransLog(img_input, const):')
    (width, height) = img_input.size
    print(f'\tNew size of image: ({width},{height})\n')

    img_output = Image.new('L', (width, height))

    for i in range(width):
        for j in range(height):
            pixel = img_input.getpixel((i,j))
            pixel = const*math.log10(1+pixel/255.0)
            img_output.putpixel((i,j), round(pixel*255))

    return img_output


def powerLow(img_input, y, c=1.0):
    """ """
    print(f'\tpowerLow(img_input, const):')
    (width, height) = img_input.size
    print(f'\tNew size of image: ({width},{height})\n')

    img_output = Image.new('L', (width, height))

    for i in range(width):
        for j in range(height):
            pixel = img_input.getpixel((i,j))
            pixel = c*pow(pixel/255.0,y)
            img_output.putpixel((i,j), round(pixel*255))

    return img_output