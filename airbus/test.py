from average import get_dom_color_img
from utils import aff_mat_2D
from utils import get_array_from_img
from utils import aff_pixel
from data_struct import ranger_image
from data_struct import associate_pixel_to_img
from merge_imgs import merge_imgs
import numpy as np

def main():

	img_noir = r"Nuit_Info_2018\airbus\img_noir.png"
	img_blanche = r"Nuit_Info_2018\airbus\img_blanche.png"
	img_res = r"Nuit_Info_2018\airbus\img_res.png"

	structure = {}
	ranger_image(structure, img_noir)
	ranger_image(structure, img_blanche)

	mat = get_array_from_img(img_res, 2, 2)
	aff_mat_2D(mat)
	map_img = np.asarray(associate_pixel_to_img(mat, structure))
	print(map_img)
	res = merge_imgs(map_img, r"C:\Users\GuillaumeGobin\Documents\Nuit_Info\Nuit_Info_2018\airbus\res.png")
	aff_mat_2D(res)

if __name__ == "__main__":
    main()

