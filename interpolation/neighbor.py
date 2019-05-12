from PIL import Image


def nearestNeighbor(img_input, factor):
    """Interpolation by nearest neighbor method

    Args:
        img_input: Image to be interpolated
        factor: Interpolation factor

    Return:
        Image interpolated
    """

    print('Function: nearestNeighbor(img_input, factor):')
    if factor == 1: 
        return img_input

    width = int(img_input.size[0]*factor)
    height = int(img_input.size[1]*factor)
    print('\tNew size of image: ({},{})\n'.format(width,height))

    img_output = Image.new('L', (width, height))
    for i in range(width):
        for j in range(height):
            pixel = (int(i/factor), int(j/factor))
            img_output.putpixel((i,j), img_input.getpixel(pixel))

    return img_output