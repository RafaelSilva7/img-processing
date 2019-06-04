from PIL import Image

LAP_DEFAULT = 1
LAP_EXTEND = 2
LAP_DEFAULT_INV = 3
LAP_EXTEND_INV = 4
SOBEL_H = 5
SOBEL_V = 6

lap_mask = {
    'lap_default' : LAP_DEFAULT,
    'lap_extend' : LAP_EXTEND,
    'lap_default_inv' : LAP_DEFAULT_INV,
    'lap_extend_inv' : LAP_EXTEND_INV,
    'sobel_h' : SOBEL_H,
    'sobel_v' : SOBEL_V
}

def applyFitler(img_input, filter, mask):
    """ """
    print('applyFitler(img_input, filter):')
    (width, height) = img_input.size
    img_output = Image.new('L', (width, height))
    print(f'\tNew size of image: ({width},{height})\n')

    print(f'filter: {filter}\nmask: {mask}')
    
    if filter == 'laplace':
        for i in range(width):
            for j in range(height):
                img_output.putpixel((i,j), laplacian(i,j, lap_mask[mask], img_input))

    elif filter == 'sobel':
        for i in range(width):
            for j in range(height):
                img_output.putpixel((i,j), sobel(i,j, lap_mask[mask], img_input))

    return img_output

# Average Filter


# Laplacian Filter
def laplacian(i, j, mask, img_input):
    """ """

    # border treatment
    if i == 0 or j == 0 or i == img_input.size[0]-1 or j == img_input.size[1]-1:
        return 0;

    # default laplacean mask
    if mask in (LAP_DEFAULT, LAP_DEFAULT_INV):
        p1 = img_input.getpixel((i+1,j))
        p2 = img_input.getpixel((i-1,j))
        p3 = img_input.getpixel((i,j+1))
        p4 = img_input.getpixel((i,j-1))
        p5 = img_input.getpixel((i,j))

        if mask == LAP_DEFAULT:
            return (p1 + p2 + p3 + p4 - 4*p5)
        else:
            return (-1*p1) + (-1*p2) + (-1*p3) + (-1*p4) + (4*p5)

    # extend laplacean mask
    else:
        p1 = img_input.getpixel((i+1,j))
        p2 = img_input.getpixel((i-1,j))
        p3 = img_input.getpixel((i,j+1))
        p4 = img_input.getpixel((i,j-1))
        p5 = img_input.getpixel((i-1,j-1))
        p6 = img_input.getpixel((i-1,j+1))
        p7 = img_input.getpixel((i+1,j-1))
        p8 = img_input.getpixel((i+1,j+1))
        p9 = img_input.getpixel((i,j))

        if mask == LAP_EXTEND:
            return (p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 - 8*p9)
        else:
            return (-1*p1) - p2 - p3 - p4 - p5 - p6 - p7 - p8 + 8*p9


# Gradient Filter
def sobel(i, j, mask, img_input):
    """ """

    # border treatment
    if i == 0 or j == 0 or i == img_input.size[0]-1 or j == img_input.size[1]-1:
        return 0;

    if mask == SOBEL_H:
        p1 = img_input.getpixel((i-1,j-1))
        p2 = img_input.getpixel((i,  j-1))
        p3 = img_input.getpixel((i+1,j-1))
        
        p4 = img_input.getpixel((i-1,j+1))
        p5 = img_input.getpixel((i,  j+1))
        p6 = img_input.getpixel((i+1,j+1))

        return (-1*p1) - 2*p2 - p3 + p4 + 2*p5 + p6

    else:
        p1 = img_input.getpixel((i-1,j-1))
        p2 = img_input.getpixel((i-1,j))
        p3 = img_input.getpixel((i-1,j+1))
        
        p4 = img_input.getpixel((i+1,j-1))
        p5 = img_input.getpixel((i+1,j))
        p6 = img_input.getpixel((i+1,j+1))

        return (-1*p1) - 2*p2 - p3 + p4 + 2*p5 + p6