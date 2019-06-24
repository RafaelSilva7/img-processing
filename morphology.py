from PIL import Image
import numpy as np
import json
from operators import arithmetic

def structuringElement(path):
    """
    """
    with open(path) as f:
        data = json.load(f)
        data['matrix'] = np.array(data['matrix'])
        data['center'] = tuple(data['center'])
    return data

def erosion(img_input, struct_path):
    """
    """
    print('erosion(img_input, struct_path):')
    (width, height) = img_input.size
    img_output = Image.new('L', (width, height))
    print(f'\tNew size of image: ({width},{height})\n')
    element = structuringElement(struct_path)

    img_output = Image.new('L', (width, height), 255)
    for j in range(height):
        for i in range(width):
            # check if it will dilate
            test = True
            if i+element['center'][0] < width and j+element['center'][1] < height:
                if img_input.getpixel((i+element['center'][0],j+element['center'][1])) == 0:
                    for k in range(element['width']):
                        for l in range(element['height']):
                            if i+k >= width or j+l >= height or img_input.getpixel((i+k,j+l)) == 255:
                                test = False
                                break
                    if test:
                        img_output.putpixel((i+element['center'][0],j+element['center'][1]), 0)

    return img_output


def dilation(img_input, struct_path):
    """
    """
    print('dilation(img_input, struct_path):')
    (width, height) = img_input.size
    img_output = Image.new('L', (width, height))
    print(f'\tNew size of image: ({width},{height})\n')
    element = structuringElement(struct_path)

    img_output = Image.new('L', (width, height), 255)
    for j in range(height):
        for i in range(width):
            # check if it will dilate
            if i+element['center'][0] < width and j+element['center'][1] < height:
                if img_input.getpixel((i+element['center'][0],j+element['center'][1])) == 0:
                    for k in range(element['width']):
                        for l in range(element['height']):
                            if element['matrix'].item((k,l)) == 255 or i+k >= width or j+l >= height:
                                pass
                            else:
                                img_output.putpixel((i+k, j+l), 0)

    return img_output


def extractContours(img_input):
    """
    """
    print('extractContours(img_input):')
    (width, height) = img_input.size
    img_output = Image.new('L', (width, height), 255)
    print(f'\tNew size of image: ({width},{height})\n')

    temp = erosion(img_input, './struct-element.json')
    
    for i in range(width):
        for j in range(height):
            if img_input.getpixel((i,j)) == 0 and temp.getpixel((i,j)) == 255:
                img_output.putpixel((i,j), 0)

    return img_output