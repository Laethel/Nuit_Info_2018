from PIL import Image 
import os 
 
 
# concatene des image de la liste d'adresse d'images "liste" 
# en mettant "width_f" nombre d'images en largeur 
# et "height_f" nombre d'image en hauteur 
 
def merge_imgs(liste, width_f, height_f): 
    img = Image.open(liste[0]) 
    width_image, height_image = img.size 
    res = Image.new("RGB",(width_f * width_image, height_f * height_image)) 
    curseur_x = 0 
    curseur_y = 0 
    for image in liste: 
        img = Image.open(image) 
        print(curseur_x,curseur_y) 
        if (curseur_x >= width_image * width_f): 
            curseur_x = 0 
            curseur_y += height_image 
        res.paste(img, box=(curseur_x, curseur_y)) 
        curseur_x += width_image 
    #res.save(r"C:\Users\VM\Desktop\py\Nuit_Info_2018\airbus\toto.jpg") 
         
    return res 
 
if __name__ == "__main__": 
    liste_images = [r"C:\Users\VM\Desktop\py\Nuit_Info_2018\airbus\test.jpg", r"C:\Users\VM\Desktop\py\Nuit_Info_2018\airbus\test2.jpg", r"C:\Users\VM\Desktop\py\Nuit_Info_2018\airbus\test2.jpg"] 
    merge_imgs(liste_images, 1, 3).show()