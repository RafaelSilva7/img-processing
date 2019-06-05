from PIL import Image

LAP_DEFAULT = 1
LAP_EXTEND = 2
LAP_DEFAULT_INV = 3
LAP_EXTEND_INV = 4
SOBEL_H = 5
SOBEL_V = 6
MEAN_3 = 7
MEAN_5 = 8

list_mask = {
    'lap_default' : LAP_DEFAULT,
    'lap_extend' : LAP_EXTEND,
    'lap_default_inv' : LAP_DEFAULT_INV,
    'lap_extend_inv' : LAP_EXTEND_INV,
    'sobel_h' : SOBEL_H,
    'sobel_v' : SOBEL_V,
    'mean_3' : MEAN_3,
    'mean_5' : MEAN_5
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
                img_output.putpixel((i,j), laplacian(i,j, list_mask[mask], img_input))

    elif filter == 'sobel':
        for i in range(width):
            for j in range(height):
                img_output.putpixel((i,j), sobel(i,j, list_mask[mask], img_input))
    
    else:
        if list_mask[mask] == MEAN_3:
            return Media3x3(img_input)
        else:
            return Media5x5(img_input)

    return img_output


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


def Media3x3(Imagem): #Filtro de Média usando mascara de 3x3
	
	Imagem = Imagem.convert("L")

	matrizImagem = Imagem.load()

	A, L = Imagem.size

	Matriz = {}

	for x in range(A):
		for y in range(L):
			Matriz[x,y] = matrizImagem[x,y]

	finalImagem = Image.new('L', (A, L))

	for x in range(A):
		for y in range(L):
			if x > 1 and y > 1 and x < A-1 and y < L-1 : #Excluir as bordas
				pixel = int((Matriz[x+1,y-1] + Matriz[x,y-1] + Matriz[x-1,y-1] + Matriz[x+1,y] + Matriz[x,y] + Matriz[x-1,y] + Matriz[x+1,y+1] + Matriz[x,y+1] + Matriz[x-1,y+1]) / 9)
				finalImagem.putpixel((x,y),pixel)
			else: #Preenche as bordas usando o Replicação
				pixel = Matriz[x,y]
				finalImagem.putpixel((x,y),pixel)
	return finalImagem


def Media5x5(Imagem): #Filtro de Média usando mascara de 3x3
	
	Imagem = Imagem.convert("L")
	
	matrizImagem = Imagem.load()

	A, L = Imagem.size

	Matriz = {}

	for x in range(A):
		for y in range(L):
			Matriz[x,y] = matrizImagem[x,y]

	finalImagem = Image.new('L', (A, L))

	for x in range(A):
		for y in range(L):
			if x > 2 and y > 2 and x < A-2 and y < L-2 : #Excluir as bordas
				pixel = int((Matriz[x+1,y-1] + Matriz[x,y-1] + Matriz[x-1,y-1] + Matriz[x+1,y] + Matriz[x,y]
							 + Matriz[x-1,y] + Matriz[x+1,y+1] + Matriz[x,y+1] + Matriz[x-1,y+1] + Matriz[x-2,y-2]
							 + Matriz[x,y-2] + Matriz[x+2,y-2] + Matriz[x+2,y] + Matriz[x-2,y-1] + Matriz[x-2,y]
							 + Matriz[x+2,y+2] + Matriz[x,y+2] + Matriz[x-2,y+2] + Matriz[x-1,y-1] + Matriz[x+2,y-1]
							 + Matriz[x+2,y+1] + Matriz[x+1,y+2] + Matriz[x-2,y+2] + Matriz[x+1,y+2] + Matriz[x+2,y+1]) / 25)
				
				finalImagem.putpixel((x,y),pixel)
			else: #Preenche as bordas usando o Replicação
				pixel = Matriz[x,y]
				finalImagem.putpixel((x,y),pixel)

	return finalImagem