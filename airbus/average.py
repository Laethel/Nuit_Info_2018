import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from utils import get_array_from_img
from utils import aff_mat_2D

def get_dom_color_img(mat):
	somR = 0
	somG = 0
	somB = 0
	nb_pixel = len(mat) * len(mat[0])
	for ligne in mat:
		for (r,g,b) in ligne:
			somR += r
			somG += g
			somB += b
	return (int(somR/nb_pixel), int(somG/nb_pixel), int(somB/nb_pixel))
