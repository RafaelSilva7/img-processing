from PIL import Image
from optparse import OptionParser
from interpolation import nearest_neighbor, bicubic, bilinear
import timeit


def config_option():
    """
    """
    parser = OptionParser(version='%prog v1.0', usage='usage: %prog [option] arg1')
    parser.add_option('-i', '--image', dest='image', metavar='PATH', help='path of the image to be used.', type='string')
    parser.add_option('-t', '--type', dest='type', metavar='TYPE', choices=('neighbor','bilinear', 'bicubic'), help='Type of interpolation to be used. {neighbor, bilinear, bicubic}')
    parser.add_option('-s', '--scale', dest='factory', help='Increase/decrease factor. [0 = 0% ,1 = 100%]')
    parser.add_option('-o', '--output', dest='output', help='Name of output image.')

    return parser


def main():
    """

    """
    (options, argvs) = config_option().parse_args()
    
    try:
        img_input = Image.open(options.image).convert('L')
        print('path of image: ' + options.image)
        print('Size of origin image: ({},{})\n'.format(img_input.size[0], img_input.size[1]))
        print(options.type)
        if options.type == 'neighbor':
            start_time = timeit.default_timer()
            img_output = nearest_neighbor(img_input, float(options.factory))
            stop_time = timeit.default_timer()

            print('Time running: %.4fs' % (stop_time - start_time))
            img_output.show()
            img_output.save('./output/'+options.output, 'PNG')  

        elif options.type == 'bilinear':
            start_time = timeit.default_timer()
            img_output = bilinear(img_input, float(options.factory))
            stop_time = timeit.default_timer()
            
            print('Time running: %.4fs' % (stop_time - start_time))
            img_output.show()
            img_output.save('./output/'+options.output, 'PNG')

        else:
            start_time = timeit.default_timer()
            img_output = bicubic(img_input, float(options.factory))
            stop_time = timeit.default_timer()

            print('Time running: %.4fs' % (stop_time - start_time))
            img_output.show()
            img_output.save('./output/'+options.output, 'PNG')
        
        print('Output image saved in: ./output/' + options.output)

    except IOError:
        print('Error: Image not found. informed path: ' + options.image + '')


if __name__ == "__main__":
    main()