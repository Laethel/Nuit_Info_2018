from average import get_dom_color_img
from utils import aff_mat_2D
from utils import get_array_from_img
from utils import aff_pixel
from data_struct import ranger_image
from data_struct import associate_pixel_to_img
from merge_imgs import merge_imgs
from PIL import Image
import numpy as np
import os
import sys

dir_bibli = r"Bibli"
dir_img_unif = r"img_unif"
chemin_img_save = r"C:\\Users\\GuillaumeGobin\\Documents\\Nuit_Info\\Nuit_Info_2018\\airbus\\res.png"
chemin_img_res = r"Limage.png"

img_res = Image.open(chemin_img_res)

(sizeX, sizeY) = img_res.size



def main():
	if len(sys.argv) == 2:
		size_mosaique = int(sys.argv[1])
		img_resizeX = sizeX
		img_resizeY = sizeY
	elif len(sys.argv) == 4:
		size_mosaique = int(sys.argv[1])
		img_resizeX = int(sys.argv[2])
		img_resizeY = int(sys.argv[3])
	else:
		print("Usage : <size_mosaique> [ <size_img_x> <size_img_y> ]")
		exit()
	nb_img = len(os.listdir(dir_bibli))
	print("Nombre d'image : ",nb_img)
	struc = {}
	print("Creation structure...")
	for i in range(1,nb_img+1):
		ranger_image(struc, i, dir_bibli, dir_img_unif, size_mosaique)
	
	mat = get_array_from_img(chemin_img_res, img_resizeX, img_resizeY)

	print("Debut association...")
	map_img = associate_pixel_to_img(mat, struc)

	print("Debut merge...")
	res = merge_imgs(map_img, chemin_img_save, size_mosaique, dir_img_unif)
	aff_mat_2D(res)


if __name__ == "__main__":
    main()

