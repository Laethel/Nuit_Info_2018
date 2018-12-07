import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

def normalize(path, sizeX, sizeY):
	img = Image.open(os.path.normpath(path))
	return img.resize((sizeX, sizeY), Image.ANTIALIAS)	

def get_array_from_img(path, sizeX, sizeY):
	img = Image.open(os.path.normpath(path))
	img = img.resize((sizeX, sizeY), Image.ANTIALIAS)
	return np.asarray(img)

def get_array_from_resized_img(img, sizeX, sizeY): #img de type Image from PIL
	img = img.resize((sizeX, sizeY), Image.ANTIALIAS)
	return np.asarray(img)

def aff_mat_2D(matrice):
	plt.imshow(matrice)
	plt.show()

def aff_pixel(rgb):
	plt.imshow([[rgb]])
	plt.show()


"""
Exemple : 
import utils
img = utils.get_array_from_img("Nuit_Info_2018\\airbus\\image.jpeg", 100, 100)
utils.aff_mat_2D(img)
"""