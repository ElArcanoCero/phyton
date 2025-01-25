import cv2
import numpy as np


imga = cv2.imread('direccion de la imagen aqui',0)  # Leemos la imagen
fil1, colum1 = imga.shape[:2]  # Obtenemos sus dimensiones filas columnas

imgFa=(np.zeros((fil1, colum1), np.uint8)) # matriz de ceros con las dimenciones de la imagen
imgFb=(np.zeros((fil1, colum1), np.uint8))# matriz de ceros con las dimenciones de la imagen
imgk1=np.array([[-3, -1, -1, -1, -3], 
               [-1, 2, 2, 2, -1],
               [-1, 2, 8, 2, -1],
               [-1, 2, 2, 2, -1]
               ,[-3, -1, -1, -1, -3]])  # filtro paso alto creado a mano o kernel
imgk2=np.array([[1, 1, 1, 1, 1], 
               [1, 2, 2, 2, 1],
               [1, 2, 8, 2, 1],
               [1, 2, 2, 2, 1]
               ,[1, 1, 1, 1, 1]])/40  # filtro paso bajo creado a mano o kernel
imgFa = cv2.filter2D(imga, ddepth=-1, kernel=imgk1, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D esto elimina los bajos extraños
imgFb= cv2.filter2D(imga, ddepth=-1, kernel=imgk2, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D esto elimina los altos extraños
cv2.imshow('original', imga)
cv2.imshow('filtro paso alto', imgFa)
cv2.imshow('filtro paso bajo', imgFb)
cv2.waitKey(0)
cv2.destroyAllWindows()
