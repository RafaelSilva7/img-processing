from PIL import Image


def bilinear(img_input, factor):
    """Interpolation by bilinear method

    Args:
        img_input: Image to be interpolated
        factor: Interpolation factor

    Return:
        Image interpolated
    """

    print('Function: bilinear(img_input, factor):')
    if factor == 1: 
        return img_input

    width = int(img_input.size[0]*factor)
    height = int(img_input.size[1]*factor)
    print('\tNew size of image: ({},{})\n'.format(width,height))

    img_output = Image.new('L', (width, height))
    flag_i = True
    flag_j = True

    for i in range(width):
        for j in range(height):
            pixel = (int(i/factor), int(j/factor))

            # Increase
            if factor > 1:
                if flag_i and flag_j:
                    img_output.putpixel((i,j), img_input.getpixel(pixel))
                elif flag_i and not flag_j:
                    v1 = img_input.getpixel(pixel)
                    v2 = img_input.getpixel((pixel[0]+1,pixel[1])) if pixel[0]+1 < img_input.size[0] else v1
                    img_output.putpixel((i,j), int((v1+v2)/2))
                elif flag_j and not flag_i:
                    v1 = img_input.getpixel(pixel)
                    v2 = img_input.getpixel((pixel[0],pixel[1]+1)) if pixel[1]+1 < img_input.size[1] else v1
                    img_output.putpixel((i,j), int((v1+v2)/2))
                else:
                    divisor = 4
                    v1 = img_input.getpixel(pixel)

                    if pixel[0]+1 < img_input.size[0]:
                        v2 = img_input.getpixel((pixel[0]+1,pixel[1]))
                    else:
                        v2 = 0
                        divisor -= 1
                    
                    if pixel[1]+1 < img_input.size[1]:
                        v3 = img_input.getpixel((pixel[0],pixel[1]+1))
                    else:
                        v3 = 0
                        divisor -= 1
                    
                    if pixel[0]+1 < img_input.size[0] and pixel[1]+1 < img_input.size[1]:
                        v4 = img_input.getpixel((pixel[0]+1,pixel[1]+1))
                    else:
                        v4 = 0
                        divisor -= 1
                    
                    img_output.putpixel((i,j), int((v1+v2+v3+v4)/divisor))

            # Decrease
            else:
                divisor = 4
                v1 = img_input.getpixel(pixel)

                if pixel[0]+1 < img_input.size[0]:
                    v2 = img_input.getpixel((pixel[0]+1,pixel[1]))
                else:
                    v2 = 0
                    divisor -= 1
                
                if pixel[1]+1 < img_input.size[1]:
                    v3 = img_input.getpixel((pixel[0],pixel[1]+1))
                else:
                    v3 = 0
                    divisor -= 1
                
                if pixel[0]+1 < img_input.size[0] and pixel[1]+1 < img_input.size[1]:
                    v4 = img_input.getpixel((pixel[0]+1,pixel[1]+1))
                else:
                    v4 = 0
                    divisor -= 1
                
                img_output.putpixel((i,j), int((v1+v2+v3+v4)/divisor))
                
            flag_j = not flag_j

        flag_i = not flag_i
    
    return img_output