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

dir_bibli = r"Nuit_Info_2018\\airbus\\Bibli"
dir_img_unif = r"Nuit_Info_2018\\airbus\\img_unif"
chemin_img_save = r"C:\\Users\\GuillaumeGobin\\Documents\\Nuit_Info\\Nuit_Info_2018\\airbus\\res.png"
chemin_img_res = r"Nuit_Info_2018\\airbus\\Limage.png"

img_res = Image.open(chemin_img_res)

(sizeX, sizeY) = img_res.size

size_mosaique = 10
img_resizeX = 10
img_resizeY = 10

def main():
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

