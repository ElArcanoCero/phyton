import cv2
import numpy as np


imga = cv2.imread('inserta la direccion de la imagen aqui',0)  # Leemos la imagen
fil1, colum1 = imga.shape[:2]   # Obtenemos sus dimensiones height alto width ancho
imgx=(np.ones((fil1, colum1), np.uint8)) # creamos matiz con el tamaño de la imagen de unos
imgc=(np.zeros((fil1, colum1), np.uint8)) # creamos matiz con el tamaño de la imagen de ceros
imgb = cv2.GaussianBlur(imga,(35,35),0) # aplicamos filtro gausiano a la imagen a
'''
for i in range(0, fil1):
    for j in range(0, colum1):
        imgc[i,j] = roun((imga[i,j]*0.3))+round((imgb[i,j]*0.7))-(imgx[i,j]*34)
        # intento de correccion de errores sumando la imagen a y b, usamamos la  matris x para la correccion de exesos
'''
imgc= cv2.addWeighted(imga, 0.3, imgb, 0.7,-34) # realizamos la suma de las imagenes

cv2.imshow('imagen 1', imga)
cv2.imshow('imagen 2', imgb)
cv2.imshow('imagen 3', imgc)
cv2.waitKey(0)
cv2.destroyAllWindows()
