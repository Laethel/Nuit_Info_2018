from PIL import Image 
import os 
from utils import normalize
import datetime
 
# concatene des image de la matrice de chemin d'image "matrix"
# sauvegarde le résultat dans le path donné "save_path"
 
def merge_imgs(matrix, save_path, sizeX, sizeY): 
	
	#img = Image.open(matrix[0][0]) 
	width_image, height_image = sizeX, sizeY
	res = Image.new("RGB",(len(matrix) * width_image, len(matrix[0]) * height_image)) 
	curseur_x = 0 
	curseur_y = 0 
	for j in matrix:
		for i in j:
			img = Image.open(r"Nuit_Info_2018\airbus\img_unif/"+str(i)+".jpg")
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