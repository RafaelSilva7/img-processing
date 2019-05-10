from PIL import Image
from optparse import OptionParser, OptionValueError
from interpolation import nearest_neighbor, bicubic, bilinear
from labeling import labeling
import timeit


def config_option():
    """
    """

    def scale_callback(option, opt, value, parser):
        """
        """
        if parser.values.type == 'labeling':
            raise OptionValueError('can\'t use -s with --type = labeling')
        elif float(value) < 0.25:
            raise OptionValueError('Increase/decrease factor must be greater than 0.25 or 25%')
        setattr(parser.values, option.dest, value)


    parser = OptionParser(version='%prog v1.0', usage='usage: %prog [option] arg1')
    parser.add_option('-i', '--image', dest='image', metavar='PATH', help='path of the image to be used.', type='string')
    parser.add_option('-t', '--type', dest='type', metavar='TYPE', choices=('neighbor','bilinear', 'bicubic', 'labeling'), help='Type of interpolation to be used. {neighbor, bilinear, bicubic, labeling}')
    parser.add_option('-s', '--scale', dest='factor', help='Increase/decrease factor. It is must be greater than 0.25 or 25%. Can\'t use with --type = labeling [0 = 0%, 1.5 = 150%]', action='callback', callback=scale_callback, type='str')
    parser.add_option('-o', '--output', dest='output', help='Name of output image. e.g: lena.png')

    return parser


def main():
    """

    """
    (options, argvs) = config_option().parse_args()
    
    try:
        print(options.type)
        if options.type != 'labeling':
            img_input = Image.open(options.image).convert('L')
        else:
            img_input = Image.open(options.image).convert('L').point(lambda x : 255 if x > 127 else 0, mode='1')

        print('path of image: ' + options.image)
        print('Size of origin image: ({},{})\n'.format(img_input.size[0], img_input.size[1]))

        if options.type == 'neighbor':
            start_time = timeit.default_timer()
            img_output = nearest_neighbor(img_input, float(options.factor))
            stop_time = timeit.default_timer()

            print('Time running: %.4fs' % (stop_time - start_time))
            img_output.show()
            img_output.save('./output/'+options.output, 'PNG')  

        elif options.type == 'bilinear':
            start_time = timeit.default_timer()
            img_output = bilinear(img_input, float(options.factor))
            stop_time = timeit.default_timer()
            
            print('Time running: %.4fs' % (stop_time - start_time))
            img_output.show()
            img_output.save('./output/'+options.output, 'PNG')

        elif options.type == 'bicubic':
            start_time = timeit.default_timer()
            img_output = bicubic(img_input, float(options.factor))
            stop_time = timeit.default_timer()

            print('Time running: %.4fs' % (stop_time - start_time))
            img_output.show()
            img_output.save('./output/'+options.output, 'PNG')
        else:
            #img_input.show()
            start_time = timeit.default_timer()
            (img_output, num_labels) = labeling(img_input)
            stop_time = timeit.default_timer()

            print('Time running: %.4fs' % (stop_time - start_time))
            img_output.show()
            img_output.save('./output/' + options.output, 'PNG')
            print('Number of objects: '+ str(num_labels))
        print('Output image saved in: ./output/' + options.output)

    except IOError:
        print('Error:\nImage not found. informed path: ' + options.image)


if __name__ == "__main__":
    main()