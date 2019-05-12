import timeit
import matplotlib.pyplot as plt
import numpy as np
from optparse import OptionParser, OptionValueError
from PIL import Image

from interpolation.neighbor import nearestNeighbor
from interpolation.linear import bilinear
from interpolation.cubic import bicubic
from label.labeling import labeling
from hist_processing.equalization import equalizeHistogram

def config_option():
    """Configure optparser object

    Args:
        None.
    Return:
        Configured optparser object.
    """

    def scale_callback(option, opt, value, parser):
        """Callback function for check scale value
        
        Args:
            option: option name.
            opt: option name short.
            value: value of option.
            parser: parser object.
        Return:
            None.
        """

        if parser.values.algorithm in ('labeling', 'equalization'):
            raise OptionValueError('can\'t use -s with --type = labeling')
        elif float(value) < 0.25:
            raise OptionValueError('Increase/decrease factor must be greater than 0.25 or 25%')
        setattr(parser.values, option.dest, value)

    choice = ('neighbor','bilinear', 'bicubic', 'labeling', 'equalization')

    parser = OptionParser(version='%prog v1.0', usage='usage: %prog -i <PATH> -a <NAME> [-s <FLOAT>] -o <NAME.png>')
    parser.add_option('-i', '--image', dest='image', metavar='PATH', help='path of the image to be used.', type='string')
    parser.add_option('-a', '--algorithm', dest='algorithm', metavar='NAME', choices=choice, help='Algorithm name to be used. {neighbor, bilinear, bicubic, labeling, equalization}')
    parser.add_option('-s', '--scale', dest='factor', metavar='FLOAT', help='Increase/decrease factor. It is must be greater than 0.25 or 25%. Can\'t use with --algorithm = labeling [0 = 0%, 1.5 = 150%]', action='callback', callback=scale_callback, type='string')
    parser.add_option('-o', '--output', dest='output', metavar='NAME.png', help='Name of output image. e.g: lena.png', type='string')

    return parser


def main():
    """
    Main function app
    """
    (options, argvs) = config_option().parse_args()
    
    try:
        print(options)
        if options.algorithm != 'labeling':
            img_input = Image.open(options.image).convert('L')
        else:
            img_input = Image.open(options.image).convert('L').point(lambda x : 255 if x > 127 else 0, mode='1')

        print('path of image: ' + options.image)
        print('Size of origin image: ({},{})\n'.format(img_input.size[0], img_input.size[1]))
        print('Algorithm: ' + options.algorithm)

        if options.algorithm == 'neighbor':
            start_time = timeit.default_timer()
            img_output = nearestNeighbor(img_input, float(options.factor))
            stop_time = timeit.default_timer()

        elif options.algorithm == 'bilinear':
            start_time = timeit.default_timer()
            img_output = bilinear(img_input, float(options.factor))
            stop_time = timeit.default_timer()

        elif options.algorithm == 'bicubic':
            start_time = timeit.default_timer()
            img_output = bicubic(img_input, float(options.factor))
            stop_time = timeit.default_timer()

        elif options.algorithm == 'labeling':
            start_time = timeit.default_timer()
            (img_output, num_labels) = labeling(img_input)
            stop_time = timeit.default_timer()
            
            print('Number of objects: '+ str(num_labels))

        else:
            start_time = timeit.default_timer()
            (img_output, hist_old) = equalizeHistogram(img_input)
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

        print('Time running: %.4fs' % (stop_time - start_time))
        img_output.save('./output/' + options.output, 'PNG')
        print('Output image saved in: ./output/' + options.output)
        img_output.show()

    except IOError:
        print('Error:\nImage not found. informed path: ' + options.image)


if __name__ == "__main__":
    main()