from average import get_dom_color_img
from utils import aff_mat_2D
from utils import get_array_from_img
from utils import aff_pixel
from data_struct import ranger_image


def main():
	structure = {}
	sizeX = 500
	sizeY = 500
	m = get_array_from_img("Nuit_Info_2018\\airbus\\image.jpeg", sizeX, sizeY)
	color_dom = get_dom_color_img(m)
	aff_mat_2D(m)
	aff_pixel(color_dom)

	ranger_image(structure, r"Nuit_Info_2018\airbus\image2.jpg")
	ranger_image(structure, r"Nuit_Info_2018\airbus\image2.jpg")


	print(structure)

if __name__ == "__main__":
    main()

