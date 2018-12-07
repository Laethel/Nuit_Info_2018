from average import get_dom_color_img
from utils import get_array_from_img
from utils import aff_mat_2D
from utils import normalize
import os
from PIL import Image 


def ranger_image(structure, numero):
	size = 10
	chemin_img = r"Nuit_Info_2018\airbus\Bibli/"+str(numero)+".jpg"
	save_dir = r"Nuit_Info_2018\airbus\img_unif/"+str(numero)+".jpg"
	m = get_array_from_img(chemin_img, size, size)
	color_dom = get_dom_color_img(m)
	if color_dom in structure :
		structure[color_dom].append(numero)
	else :
		structure[color_dom] = [numero]
	img = normalize(chemin_img, size, size)
	img.save(save_dir)

def get_val(rgb, structure):
	(r, g, b) = rgb
	if (r, g, b) in structure:
		return structure[(r,g,b)]
	else :
		liste = []
		for (r1,g1,b1) in structure:
			liste.append(((r1,g1,b1),abs(r-r1) + abs(g-g1) + abs(b-b1)))
		mini = ((0,0,0),255*3)
		for l in liste:
			if l[1] < mini[1] :
				mini = l
		return structure[mini[0]][0]
		
def associate_pixel_to_img(img, structure):
	return [[get_val(rgb, structure) for rgb in ligne] for ligne in img]
