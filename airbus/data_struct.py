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
		return structure[mini[0]]
		
def associate_pixel_to_img(img, structure):
	return [[get_val((r,g,b), structure) for (r,g,b) in ligne] for ligne in img]