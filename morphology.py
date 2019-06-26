from PIL import Image
import numpy as np
import json
from operators import arithmetic

def structuringElement(path):
    """
    """
    with open(path) as f:
        data = json.load(f)
        data['matrix'] = np.array(data['matrix'])
        data['center'] = tuple(data['center'])
    return data



def erosion(img_input, struct_path):
    """
    """
    print('erosion(img_input, struct_path):')
    (width, height) = img_input.size
    img_output = Image.new('L', (width, height))
    print(f'\tNew size of image: ({width},{height})\n')
    element = structuringElement(struct_path)

    img_output = Image.new('L', (width, height), 255)
    for j in range(height):
        for i in range(width):
            # check if it will dilate
            test = True
            if i+element['center'][0] < width and j+element['center'][1] < height:
                if img_input.getpixel((i+element['center'][0],j+element['center'][1])) == 0:
                    for k in range(element['width']):
                        for l in range(element['height']):
                            if i+k >= width or j+l >= height or img_input.getpixel((i+k,j+l)) == 255:
                                test = False
                                break
                    if test:
                        img_output.putpixel((i+element['center'][0],j+element['center'][1]), 0)

    return img_output



def dilation(img_input, struct_path):
    """
    """
    print('dilation(img_input, struct_path):')
    (width, height) = img_input.size
    img_output = Image.new('L', (width, height))
    print(f'\tNew size of image: ({width},{height})\n')
    element = structuringElement(struct_path)

    img_output = Image.new('L', (width, height), 255)
    for j in range(height):
        for i in range(width):
            # check if it will dilate
            if i+element['center'][0] < width and j+element['center'][1] < height:
                if img_input.getpixel((i+element['center'][0],j+element['center'][1])) == 0:
                    for k in range(element['width']):
                        for l in range(element['height']):
                            if element['matrix'].item((k,l)) == 255 or i+k >= width or j+l >= height:
                                pass
                            else:
                                img_output.putpixel((i+k, j+l), 0)

    return img_output



def extractContours(img_input):
    """
    """
    print('extractContours(img_input):')
    (width, height) = img_input.size
    img_output = Image.new('L', (width, height), 255)
    print(f'\tNew size of image: ({width},{height})\n')

    temp = erosion(img_input, './struct-element.json')
    
    for i in range(width):
        for j in range(height):
            if img_input.getpixel((i,j)) == 0 and temp.getpixel((i,j)) == 255:
                img_output.putpixel((i,j), 0)

    return img_output



def opening(img_input, struct_path):
    """
    """
    print('opening(img_input, struct_path):')
    (width, height) = img_input.size
    print(f'\tNew size of image: ({width},{height})\n')

    temp = erosion(img_input, struct_path)
    return dilation(temp, struct_path)    



def ending(img_input, struct_path):
    """
    """
    print('ending(img_input, struct_path):')
    (width, height) = img_input.size
    print(f'\tNew size of image: ({width},{height})\n')

    temp = dilation(img_input, struct_path)
    return erosion(temp, struct_path)  



def erosionGray3(Imagem):
    """
    """
	matrizImagem = Imagem.load()
	A, L = Imagem.size
	Matriz = {}

	for x in range(A):
		for y in range(L):
			Matriz[x,y] = matrizImagem[x,y]

	finalImagem = Image.new('L', (A, L))

	for x in range(A):
		for y in range(L):
			if x > 1 and y > 1 and x < A-1 and y < L-1 :
				pixel = min(Matriz[x,y], Matriz[x-1,y], Matriz[x+1,y], Matriz[x,y+1], Matriz[x,y-1])
				finalImagem.putpixel((x,y),pixel)
			else:
				pixel = Matriz[x,y]
				finalImagem.putpixel((x,y),pixel)

	return finalImagem


def erosionGray5(Imagem):
    """
    """
	matrizImagem = Imagem.load()
	A, L = Imagem.size
	Matriz = {}

	for x in range(A):
		for y in range(L):
			Matriz[x,y] = matrizImagem[x,y]

	finalImagem = Image.new('L', (A, L))

	for x in range(A):
		for y in range(L):
			if x > 2 and y > 2 and x < A-2 and y < L-2 :
				pixel = pixel = min(Matriz[x+1,y-1], Matriz[x,y-1], Matriz[x-1,y-1], Matriz[x+1,y], Matriz[x,y]
							 + Matriz[x-1,y], Matriz[x+1,y+1], Matriz[x,y+1], Matriz[x-1,y+1], Matriz[x-2,y-2]
							 + Matriz[x,y-2], Matriz[x+2,y-2], Matriz[x+2,y], Matriz[x-2,y-1], Matriz[x-2,y]
							 + Matriz[x+2,y+2], Matriz[x,y+2], Matriz[x-2,y+2], Matriz[x-1,y-1], Matriz[x+2,y-1]
							 + Matriz[x+2,y+1], Matriz[x+1,y+2], Matriz[x-2,y+2], Matriz[x+1,y+2], Matriz[x+2,y+1])
				finalImagem.putpixel((x,y),pixel)
			else:
				pixel = Matriz[x,y]
				finalImagem.putpixel((x,y),pixel)

	return finalImagem


def dilationGray3(Imagem):
    """
    """
	matrizImagem = Imagem.load()
	A, L = Imagem.size
	Matriz = {}

	for x in range(A):
		for y in range(L):
			Matriz[x,y] = matrizImagem[x,y]

	finalImagem = Image.new('L', (A, L))

	for x in range(A):
		for y in range(L):
			if x > 1 and y > 1 and x < A-1 and y < L-1 :
				pixel = max(Matriz[x,y], Matriz[x-1,y], Matriz[x+1,y], Matriz[x,y+1], Matriz[x,y-1])
				finalImagem.putpixel((x,y),pixel)
			else:
				pixel = Matriz[x,y]
				finalImagem.putpixel((x,y),pixel)

	return finalImagem



def dilationGray5(Imagem):
    """
    """
	matrizImagem = Imagem.load()
	A, L = Imagem.size
	Matriz = {}

	for x in range(A):
		for y in range(L):
			Matriz[x,y] = matrizImagem[x,y]

	finalImagem = Image.new('L', (A, L))

	for x in range(A):
		for y in range(L):
			if x > 2 and y > 2 and x < A-2 and y < L-2 :
				pixel = pixel = max(Matriz[x+1,y-1], Matriz[x,y-1], Matriz[x-1,y-1], Matriz[x+1,y], Matriz[x,y]
							 + Matriz[x-1,y], Matriz[x+1,y+1], Matriz[x,y+1], Matriz[x-1,y+1], Matriz[x-2,y-2]
							 + Matriz[x,y-2], Matriz[x+2,y-2], Matriz[x+2,y], Matriz[x-2,y-1], Matriz[x-2,y]
							 + Matriz[x+2,y+2], Matriz[x,y+2], Matriz[x-2,y+2], Matriz[x-1,y-1], Matriz[x+2,y-1]
							 + Matriz[x+2,y+1], Matriz[x+1,y+2], Matriz[x-2,y+2], Matriz[x+1,y+2], Matriz[x+2,y+1])
				finalImagem.putpixel((x,y),pixel)
			else:
				pixel = Matriz[x,y]
				finalImagem.putpixel((x,y),pixel)

	return finalImagem