from average import get_dom_color_img
from utils import get_array_from_img
from utils import aff_mat_2D

def ranger_image(structure, path):
	size = 10
	m = get_array_from_img(path, size, size)
	color_dom = get_dom_color_img(m)
	if color_dom in structure :
		structure[color_dom].append(path)
	else :
		structure[color_dom] = [path]

def associate_pixel_to_img(img, structure):
	return [[get_val((r,g,b), structure) for (r,g,b) in ligne] for ligne in img]

def get_val(rgb, structure):	
	(r, g, b) = rgb
	if (r, g, b) in structure:
		return structure[(r,g,b)]
	else :
		l = []
		for (a,b,c) in structure:
			l.append((r-a, g-b, b-c))

struc = {}
struc[(0,0,0)] = 1
struc[(255,255,255)] = 2
for i in struc:
	print(i)