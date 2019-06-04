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


def bicubic(img_input, factor):
    """Interpolation by bicubic method

    Args:
        img_input: Image to be interpolated
        factor: Interpolation factor

    Return:
        Image interpolated
    """

    print('Function: bicubic(img_input, factor):')
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
                
                # a = (f(i,j) + f(i,j+1)+ f(i,j+2) )/ 3 and e = (f(i+1,j) + f(i+1,j+1) + f(i+1,j+2) ) / 3
                elif flag_i and not flag_j:
                    d = 3 # divisor
                    v1 = img_input.getpixel(pixel)
                    if pixel[0]+1 < img_input.size[0]:
                        v2 = img_input.getpixel((pixel[0]+1,pixel[1]))
                    else:
                        v2 = 0
                        d -= 1
                    
                    if pixel[0]+2 < img_input.size[0]:
                        v3 = img_input.getpixel((pixel[0]+2,pixel[1]))
                    else:
                        v3 = 0
                        d -= 1

                    img_output.putpixel((i,j), int((v1+v2+v3)/d))

                # b = (f(i,j) + f(i+1,j)+f(i+2,j) )/ 3 and d = (f(i,j+1) + f(i+1,j+1)+f(i+2,j+1)) /3
                elif flag_j and not flag_i:
                    d = 3 # divisor
                    v1 = img_input.getpixel(pixel)
                    if pixel[1]+1 < img_input.size[1]:
                        v2 = img_input.getpixel((pixel[0],pixel[1]+1))
                    else:
                        v2 = 0
                        d -= 1
                    
                    if pixel[1]+2 < img_input.size[1]:
                        v3 = img_input.getpixel((pixel[0],pixel[1]+2))
                    else:
                        v3 = 0
                        d -= 1

                    img_output.putpixel((i,j), int((v1+v2+v3)/d))
                # c = (f(i,j) + f(i,j+1) + f(i+1,j) + f(i+1,j+1)+ f(i+2,j)+f(i+2,j+1) +f(i+2,j+2)+ f(i,j+2)+f(i+1,j+2)) / 9
                else:
                    d = 9 # divisor
                    v1 = img_input.getpixel(pixel)
                    if pixel[0]+2 < img_input.size[0]:
                        v2 = img_input.getpixel((pixel[0]+1,pixel[1]))
                        v3 = img_input.getpixel((pixel[0]+2,pixel[1]))
                    elif pixel[0]+1 < img_input.size[0]:
                        v2 = img_input.getpixel((pixel[0]+1,pixel[1]))
                        v3 = 0
                        d -= 1
                    else:
                        v2 = v3 = 0
                        d-= 2
                    
                    if pixel[1]+1 < img_input.size[1]:
                        v4 = img_input.getpixel((pixel[0], pixel[1]+1))
                        if pixel[0]+2 < img_input.size[0]:
                            v5 = img_input.getpixel((pixel[0]+1,pixel[1]+1))
                            v6 = img_input.getpixel((pixel[0]+2,pixel[1]+1))
                        elif pixel[0]+1 < img_input.size[0]:
                            v5 = img_input.getpixel((pixel[0]+1,pixel[1]+1))
                            v6 = 0
                            d -= 1
                        else:
                            v5 = v6 = 0
                            d-= 2
                    else:
                        v4 = v5 = v6 = 0
                        d-= 3

                    if pixel[1]+2 < img_input.size[1]:
                        v7 = img_input.getpixel((pixel[0], pixel[1]+2))
                        if pixel[0]+2 < img_input.size[0]:
                            v8 = img_input.getpixel((pixel[0]+1,pixel[1]+2))
                            v9 = img_input.getpixel((pixel[0]+2,pixel[1]+2))
                        elif pixel[0]+1 < img_input.size[0]:
                            v8 = img_input.getpixel((pixel[0]+1,pixel[1]+2))
                            v9 = 0
                            d -= 1
                        else:
                            v8 = v9 = 0
                            d-= 2
                    else:
                        v7 = v8 = v9 = 0
                        d-= 3
                    
                    img_output.putpixel((i,j), int((v1+v2+v3+v4+v5+v6+v7+v8+v9)/d))

            # Decrease
            else:
                d = 9 # divisor
                v1 = img_input.getpixel(pixel)
                if pixel[0]+2 < img_input.size[0]:
                    v2 = img_input.getpixel((pixel[0]+1,pixel[1]))
                    v3 = img_input.getpixel((pixel[0]+2,pixel[1]))
                elif pixel[0]+1 < img_input.size[0]:
                    v2 = img_input.getpixel((pixel[0]+1,pixel[1]))
                    v3 = 0
                    d -= 1
                else:
                    v2 = v3 = 0
                    d-= 2
                
                if pixel[1]+1 < img_input.size[1]:
                    v4 = img_input.getpixel((pixel[0], pixel[1]+1))
                    if pixel[0]+2 < img_input.size[0]:
                        v5 = img_input.getpixel((pixel[0]+1,pixel[1]+1))
                        v6 = img_input.getpixel((pixel[0]+2,pixel[1]+1))
                    elif pixel[0]+1 < img_input.size[0]:
                        v5 = img_input.getpixel((pixel[0]+1,pixel[1]+1))
                        v6 = 0
                        d -= 1
                    else:
                        v5 = v6 = 0
                        d-= 2
                else:
                    v4 = v5 = v6 = 0
                    d-= 3

                if pixel[1]+2 < img_input.size[1]:
                    v7 = img_input.getpixel((pixel[0], pixel[1]+2))
                    if pixel[0]+2 < img_input.size[0]:
                        v8 = img_input.getpixel((pixel[0]+1,pixel[1]+2))
                        v9 = img_input.getpixel((pixel[0]+2,pixel[1]+2))
                    elif pixel[0]+1 < img_input.size[0]:
                        v8 = img_input.getpixel((pixel[0]+1,pixel[1]+2))
                        v9 = 0
                        d -= 1
                    else:
                        v8 = v9 = 0
                        d-= 2
                else:
                    v7 = v8 = v9 = 0
                    d-= 3
                
                img_output.putpixel((i,j), int((v1+v2+v3+v4+v5+v6+v7+v8+v9)/d))
                
            flag_j = not flag_j

        flag_i = not flag_i
    
    return img_output