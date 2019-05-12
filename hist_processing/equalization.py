from PIL import Image
import numpy as np

def equalizeHistogram(img_input):
    """Equalize image histogram

    Args:
        img_input: Image to be equalized

    Return:
        Equalized image and old histogram
    """

    print('\tFunction: equalization(img_input):')
    (width, height) = img_input.size
    print('\tNew size of image: ({},{})\n'.format(width,height))

    img_output = Image.new('L', (width, height))
    num_pixel = width*height
    hist_old = np.zeros(256)
    pr_rk = np.zeros(256)
    freq = np.zeros(256)
    eq = np.zeros(256)

    # get frequency
    for i in range(width):
        for j in range(height):
            color = img_input.getpixel((i,j))
            hist_old[color] += 1
    
    # get Pr(rk)
    for i in range(256):
        pr_rk[i] = hist_old[i] / num_pixel

    # get Freq
    freq[0] = pr_rk[0]
    for i in range(1,256):
        freq[i] = pr_rk[i] + freq[i-1]

    # get EQ
    for i in range(256):
        eq[i] = freq[i]*255

    # equalize image
    for i in range(width):
        for j in range(height):
            color = img_input.getpixel((i,j))
            img_output.putpixel((i,j), int(round(eq[color])))

    return (img_output, hist_old)