from PIL import Image


def nearest_neighbor(img_input, factory):
    """
    """
    print('Function: nearest_neighbor(img_input, factory):')
    if factory == 1: 
        return img_input

    width = int(img_input.size[0]*factory)
    height = int(img_input.size[1]*factory)
    print('\tNew size of image: ({},{})\n'.format(width,height))

    img_output = Image.new('L', (width, height))
    for i in range(width):
        for j in range(height):
            pixel = (int(i/factory), int(j/factory))
            img_output.putpixel((i,j), img_input.getpixel(pixel))

    return img_output


def bilinear(img_input, factory):
    """
    """
    print('Function: bilinear(img_input, factory):')
    if factory == 1: 
        return img_input

    width = int(img_input.size[0]*factory)
    height = int(img_input.size[1]*factory)
    print('\tNew size of image: ({},{})\n'.format(width,height))

    img_output = Image.new('L', (width, height))
    flag_i = False
    flag_j = False

    for i in range(width):
        for j in range(height):
            # Increase
            if factory > 1:
                pixel = (int(i/factory), int(j/factory))
                if flag_i and flag_j:
                    img_output.putpixel((i,j), img_input.getpixel(pixel))
                elif flag_i and not flag_j:
                    v1 = img_input.getpixel(pixel)
                    v2 = img_input.getpixel((pixel[0]+1,pixel[1])) if i < img_input.size[0] else v1
                    img_output.putpixel((i,j), int((v1+v2)/2))
                elif flag_j and not flag_i:
                    v1 = img_input.getpixel(pixel)
                    v2 = img_input.getpixel((pixel[0],pixel[1]+1)) if j < img_input.size[1] else v1
                    img_output.putpixel((i,j), int((v1+v2)/2))
                else:
                    v1 = img_input.getpixel(pixel)
                    v2 = img_input.getpixel((pixel[0]+1,pixel[1])) if i < img_input.size[0] else v1
                    v3 = img_input.getpixel((pixel[0],pixel[1]+1)) if j < img_input.size[1] else v1
                    v4 = img_input.getpixel((pixel[0]+1,pixel[1]+1)) if j < img_input.size[1] and i < img_input.size[0] else v1
                    img_output.putpixel((i,j), int((v1+v2+v3+v4)/4))

            # Decrease
            else:
                pass
                
            flag_j = not flag_j

        flag_i = not flag_i
    
    return img_output

def bicubic(img_input, factory):
    """
    """
    print('Function: bicubic(img_input, factory):')
    width = int(img_input.size[0]*factory)
    height = int(img_input.size[1]*factory)
    print('\tNew size of image: ({},{})\n'.format(width,height))

    img_output = Image.new('L', (width, height))
