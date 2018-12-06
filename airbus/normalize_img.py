import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
imgpil = Image.open("Nuit_Info_2018\\airbus\\image.jpeg")  
img = np.asarray(imgpil)
print(img)