from PIL import Image

def add(img1, img2, weight1=1, weight2=1):
    """ """
    print('\tadd(img1, img2, weight1=1, weight2=1):')
    width = img1.size[0] if img1.size[0] >= img2.size[0] else img2.size[0]
    height = img1.size[1] if img1.size[1] >= img2.size[1] else img2.size[1]
    print(f'\tNew size of image: ({width},{height})\n')

    img_output = Image.new('L', (width, height))

    for j in range(height):
        for i in range(width):
            p1 = img1.getpixel((i,j)) if i < img1.size[0] and j < img1.size[1] else 0
            p2 = img2.getpixel((i,j)) if i < img2.size[0] and j < img2.size[1] else 0
            new = round((p1*weight1) + (p2*weight2))

            if new < 0:
                new = 0
            elif new > 255:
                new = 255

            img_output.putpixel((i,j), new)
            
    return img_output


def division(img1, img2, weight1=1, weight2=1):
    """ """
    print('\tdivison(img1, img2, weight1=1, weight2=1):')
    width = img1.size[0] if img1.size[0] >= img2.size[0] else img2.size[0]
    height = img1.size[1] if img1.size[1] >= img2.size[1] else img2.size[1]
    print(f'\tNew size of image: ({width},{height})\n')

    img_output = Image.new('L', (width, height))

    for j in range(height):
        for i in range(width):
            p1 = img1.getpixel((i,j)) if i < img1.size[0] and j < img1.size[1] else 0
            p2 = img2.getpixel((i,j)) if i < img2.size[0] and j < img2.size[1] else 0
            new = round((p1*weight1) / (p2*weight2))

            if new < 0:
                new = 0
            elif new > 255:
                new = 255

            img_output.putpixel((i,j), new)
            
    return img_output


def multiply(img1, img2, weight1=1, weight2=1):
    """ """
    print(f'\tmultiply(img1, img2, weight1={weight1}, weight2={weight2}):')
    width = img1.size[0] if img1.size[0] >= img2.size[0] else img2.size[0]
    height = img1.size[1] if img1.size[1] >= img2.size[1] else img2.size[1]
    print(f'\tNew size of image: ({width},{height})\n')

    img_output = Image.new('L', (width, height))

    for j in range(height):
        for i in range(width):
            p1 = img1.getpixel((i,j)) if i < img1.size[0] and j < img1.size[1] else 0
            p2 = img2.getpixel((i,j)) if i < img2.size[0] and j < img2.size[1] else 0
            new = round((p1*weight1) * (p2*weight2))

            if new < 0:
                new = 0
            elif new > 255:
                new = 255

            img_output.putpixel((i,j), new)
            
    return img_output


def subtract(img1, img2, weight1=1, weight2=1):
    """ """
    print(f'\tsubtract(img1, img2, weight1={weight1}, weight2={weight2}):')
    width = img1.size[0] if img1.size[0] >= img2.size[0] else img2.size[0]
    height = img1.size[1] if img1.size[1] >= img2.size[1] else img2.size[1]
    print(f'\tNew size of image: ({width},{height})\n')

    img_output = Image.new('L', (width, height))

    for j in range(height):
        for i in range(width):
            p1 = img1.getpixel((i,j)) if i < img1.size[0] and j < img1.size[1] else 0
            p2 = img2.getpixel((i,j)) if i < img2.size[0] and j < img2.size[1] else 0
            new = round((p1*weight1) - (p2*weight2))

            if new < 0:
                new = 0
            elif new > 255:
                new = 255

            img_output.putpixel((i,j), new)
            
    return img_output