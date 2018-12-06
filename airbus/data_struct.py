from average import get_dom_color_img
from utils import get_array_from_img

def ranger_image(structure, path):
	size = 10
	m = get_array_from_img(path, size, size)
	color_dom = get_dom_color_img(m)
	if color_dom in structure :
		structure[color_dom].append(path)
	else :
		structure[color_dom] = [path]

