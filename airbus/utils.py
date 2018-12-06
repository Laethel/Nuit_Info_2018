import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def get_array_from_img(path, sizeX, sizeY):
	img = Image.open(path)
	img = img.resize((sizeX, sizeY), Image.ANTIALIAS)
	return np.asarray(img)

def aff_mat_2D(matrice):
	plt.imshow(matrice)
	plt.show()


"""
Exemple : 
import utils
img = utils.get_array_from_img("Nuit_Info_2018\\airbus\\image.jpeg", 100, 100)
utils.aff_mat_2D(img)
"""