import timeit
import matplotlib.pyplot as plt
import numpy as np
from optparse import OptionParser, OptionValueError
from PIL import Image

from operators import arithmetic, geometric
import filters, interpolation, transformation, hist_processing, label


def config_option():
    """Configure optparser object"""

    choice = ('neighbor','bilinear', 'bicubic', 'labeling', 'equalize', 'rotate', 
              'add', 'division', 'multiply', 'subtract', 'transLog', 'powerLow',
              'mirrorH', 'mirrorV', 'laplace', 'gradient', 'sobel')

    parser = OptionParser(version='%prog v1.0', usage='usage: %prog -i <path> -a <algorithm> [args]')
    parser.add_option('-i', '--image', dest='image', metavar='path', help='path of the image to be used.', type='string')
    parser.add_option('-a', '--algorithm', dest='algorithm', metavar='name', choices=choice, help='Algorithm name to be used. List in README.md')
    parser.add_option('-f', '--factor', dest='factor', metavar='float', help='Increase/decrease for interpolation and constant for the logarithmic transformation algorithm.', type='string')
    parser.add_option('-o', '--output', dest='output', metavar='name.png', help='Name of output image. e.g: lena.png', type='string')
    parser.add_option('-m', '--mask', dest='mask', metavar='name', help='Mask name of filtering algorithms')

    return parser


def checkParser(parser, argvs):
        """Callback function for check num of image"""

        if parser.algorithm in ('neighbor','bilinear', 'bicubic') and (parser.factor is None or float(parser.factor) < 0.25):
            raise OptionValueError('use --scale with --type = {neighbor,bilinear, bicubic}, the value must be greater than 0.25')
        
        if parser.algorithm in ('add', 'division', 'multiply', 'subtract') and (len(argvs) == 0 or parser.factor != None):
            raise OptionValueError('the selected algorithm must have two images as parameter and without --scale.')

        if parser.algorithm is 'transLog' and (parser.factor is None):
            raise OptionValueError('the selected algorithm must have --factor parameter.')


def main():
    """Main function app"""

    (options, argvs) = config_option().parse_args()
    checkParser(options, argvs)

    try:
        if options.algorithm == 'labeling':
            img_input = Image.open(options.image).convert('L').point(lambda x : 255 if x > 127 else 0, mode='1')
        else:
            img_input = Image.open(options.image).convert('L')

        print(f'path of image: {options.image}')
        print(f'Size of origin image: ({img_input.size[0]},{img_input.size[1]})\n')
        
        if options.algorithm in ('add', 'division', 'multiply', 'subtract'):
            img2_input = Image.open(argvs[0]).convert('L')
            print(f'path of image2: {argvs[0]}')
            print(f'Size of origin image2: ({img2_input.size[0]},{img2_input.size[1]})\n')

    except IOError:
        print(f'Error:\nImage not found. informed path: {options.image}')
        if len(argvs) == 1:
            print(f'or Image2 not found. informed path: {argvs}')
        return

    if options.algorithm == 'neighbor':
        start_time = timeit.default_timer()
        img_output = interpolation.nearestNeighbor(img_input, float(options.factor))
        stop_time = timeit.default_timer()

    elif options.algorithm == 'bilinear':
        start_time = timeit.default_timer()
        img_output = interpolation.bilinear(img_input, float(options.factor))
        stop_time = timeit.default_timer()

    elif options.algorithm == 'bicubic':
        start_time = timeit.default_timer()
        img_output = interpolation.bicubic(img_input, float(options.factor))
        stop_time = timeit.default_timer()

    elif options.algorithm == 'labeling':
        start_time = timeit.default_timer()
        (img_output, num_labels) = label.labeling(img_input)
        stop_time = timeit.default_timer()
        
        print('Number of objects: '+ str(num_labels))

    elif options.algorithm == 'equalize':
        start_time = timeit.default_timer()
        (img_output, hist_old) = hist_processing.equalize(img_input)
        stop_time = timeit.default_timer()

        hist_new = np.zeros(256)
        # get new frequency
        for i in range(img_input.size[0]):
            for j in range(img_input.size[1]):
                color = img_output.getpixel((i,j))
                hist_new[color] += 1
        
        plt.figure(1)
        
        plt.subplot(311)
        plt.plot(hist_old)
        plt.title('Old Histogram')
        plt.ylabel('Number of pixel')
        plt.xlabel('Grayscale')

        plt.subplot(212)
        plt.plot(hist_new)
        plt.title('Equalizated Histogram')
        plt.ylabel('Number of pixel')
        plt.xlabel('Grayscale')
        plt.subplots_adjust(hspace=0.15)

        plt.show()

    elif options.algorithm == 'add':
        start_time = timeit.default_timer()
        if len(argvs) == 3:
            img_output = arithmetic.add(img_input, img2_input, weight1=float(argvs[1]), weight2=float(argvs[2]))
        else:
                img_output = arithmetic.add(img_input, img2_input)
        stop_time = timeit.default_timer()

    elif options.algorithm == 'division':
        start_time = timeit.default_timer()
        if len(argvs) == 3:
            img_output = arithmetic.division(img_input, img2_input, weight1=float(argvs[1]), weight2=float(argvs[2]))
        else:
                img_output = arithmetic.division(img_input, img2_input)
        stop_time = timeit.default_timer()

    elif options.algorithm == 'multiply':
        start_time = timeit.default_timer()
        if len(argvs) == 3:
            img_output = arithmetic.multiply(img_input, img2_input, weight1=float(argvs[1]), weight2=float(argvs[2]))
        else:
                img_output = arithmetic.multiply(img_input, img2_input)
        stop_time = timeit.default_timer()
    
    elif options.algorithm == 'subtract':
        start_time = timeit.default_timer()
        if len(argvs) == 3:
            img_output = arithmetic.subtract(img_input, img2_input, weight1=float(argvs[1]), weight2=float(argvs[2]))
        else:
                img_output = arithmetic.subtract(img_input, img2_input)
        stop_time = timeit.default_timer()

    elif options.algorithm == 'transLog':
        start_time = timeit.default_timer()
        img_output = transformation.logarithmic(img_input, float(options.factor))
        stop_time = timeit.default_timer()

    elif options.algorithm == 'powerLow':
        start_time = timeit.default_timer()
        if len(argvs) == 1:
            img_output = transformation.powerLow(img_input, float(options.factor), float(argvs[0]))
        else:
            img_output = transformation.powerLow(img_input, float(options.factor))
        stop_time = timeit.default_timer()

    elif options.algorithm == 'rotate':
        start_time = timeit.default_timer()
        img_output = geometric.rotate(img_input, float(options.factor))
        stop_time = timeit.default_timer()

    elif options.algorithm == 'mirrorH':
        start_time = timeit.default_timer()
        img_output = geometric.mirrorHorizontal(img_input)
        stop_time = timeit.default_timer()

    elif options.algorithm == 'mirrorV':
        start_time = timeit.default_timer()
        img_output = geometric.mirrorVertical(img_input)
        stop_time = timeit.default_timer()

    elif options.algorithm in ('laplace', 'sobel'):
        start_time = timeit.default_timer()
        img_output = filters.applyFitler(img_input, options.algorithm, options.mask)
        stop_time = timeit.default_timer()


    print('Time running: %.4fs' % (stop_time - start_time))
    img_output.save('./output/' + options.output, 'PNG')
    print('Output image saved in: ./output/' + options.output)
    img_output.show()


if __name__ == "__main__":
    main()