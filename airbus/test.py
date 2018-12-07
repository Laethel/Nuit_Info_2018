from average import get_dom_color_img
from utils import aff_mat_2D
from utils import get_array_from_img
from utils import aff_pixel
from data_struct import ranger_image
from data_struct import associate_pixel_to_img
from merge_imgs import merge_imgs
import numpy as np

def main():
	nb_img = 31
	chemin_img_res = r"C:\Users\GuillaumeGobin\Documents\Nuit_Info\Nuit_Info_2018\airbus\res.png"
	struc = {}
	print("Creation structure")
	for i in range(1,nb_img+1):
		ranger_image(struc, i)
	img_res = r"Nuit_Info_2018\airbus\Limage.png"
	mat = get_array_from_img(img_res, 1000, 1000)

	print("Debut association")
	map_img = associate_pixel_to_img(mat, struc)

	print("Debut merge")
	res = merge_imgs(map_img, chemin_img_res, 10, 10)
	aff_mat_2D(res)

if __name__ == "__main__":
    main()
