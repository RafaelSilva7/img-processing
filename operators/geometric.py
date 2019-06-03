from PIL import Image
import math

def rotate(img_input, degree):
    """ """

    print('\tadd(img1, img2, weight1=1, weight2=1):')
    (width, height) = img_input.size
    print(f'\tNew size of image: ({width},{height})\n')

    # horizontal image
    if degree < 90 or (degree >= 180 and degree < 270):   
        img_output = Image.new('L', (width, height))
    # vertical image
    else:
        img_output = Image.new('L', (height, width))

    for i in range(width):
        for j in range(height):
            pixel = img_input.getpixel((i,j))
            origin = (int(width/2), int(height/2))
            x = int((i)*math.cos(math.radians(degree)) - (j)*math.sin(math.radians(degree)))
            y = int((i)*math.cos(math.radians(degree)) + (j)*math.sin(math.radians(degree)))

            #(x, y) = (x+origin[0], y+origin[1])
            if x < img_output.size[0] and y < img_output.size[1]:
                img_output.putpixel((x,y), pixel)

    return img_output


def mirrorHorizontal(img_input):
    """ """
    matrizImagem = img_input.load()
    A, L = img_input.size

    Matriz = {}

    for x in range(A):
        for y in range(L):
            Matriz[x,y] = matrizImagem[x,y]

    finalImagem = Image.new('L', (A, L))

    for x in range(A):
        for y in range(L):
            v = x 
            w = (L - 1) - y
            pixel = Matriz[v,w]
            finalImagem.putpixel((x,y), pixel)

    return finalImagem


def mirrorVertical(img_input):

	matrizImagem = img_input.load()
	A, L = img_input.size

	Matriz = {}

	for x in range(A):
		for y in range(L):
			Matriz[x,y] = matrizImagem[x,y]

	finalImagem = Image.new('L', (A, L))

	for x in range(A):
		for y in range(L):
			v = ( A - 1 ) - x
			w = y
			pixel = Matriz[v,w]
			finalImagem.putpixel((x,y),pixel)

	return finalImagem
    