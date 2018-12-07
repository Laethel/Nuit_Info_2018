from PIL import Image 
import os 
from utils import normalize
import datetime
 
# concatene des image de la matrice de chemin d'image "matrix"
# sauvegarde le résultat dans le path donné "save_path"
 
def merge_imgs(matrix, save_path, size, dir_img_unif): 
	width_image, height_image = size, size
	res = Image.new("RGB",(len(matrix) * width_image, len(matrix[0]) * height_image)) 
	curseur_x = 0 
	curseur_y = 0 
	for c,j in enumerate(matrix):
		print((c/len(matrix))*100,"%")
		for i in j:
			img_unif = os.path.join(dir_img_unif,str(i)+".jpg")
			img = Image.open(img_unif)
			if (curseur_x >= width_image * len(matrix) ): 
				curseur_x = 0 
				curseur_y += height_image 
			res.paste(img, box=(curseur_x, curseur_y)) 
			curseur_x += width_image 
	res.save(save_path) 
	
	return res 
 
# if __name__ == "__main__": 
#	  liste_images = [[r"C:\Users\VM\Desktop\py\Nuit_Info_2018\airbus\image.jpeg", r"C:\Users\VM\Desktop\py\Nuit_Info_2018\airbus\image.jpeg"], [r"C:\Users\VM\Desktop\py\Nuit_Info_2018\airbus\image.jpeg", r"C:\Users\VM\Desktop\py\Nuit_Info_2018\airbus\image.jpeg"] ]
#	  merge_imgs(liste_images,r"C:\Users\VM\Desktop\py\Nuit_Info_2018\airbus\toto.jpg").show()