import matplotlib.pyplot as plt
import numpy as np


def get_array_from_img(path):
	return np.asarray(plt.imread(path))

def aff_mat_2D(matrice):
	plt.imshow(matrice)
	plt.show()