import cv2
import numpy as np

# Variables globales
selected_color = None

# Función para manejar el clic del mouse
def select_color(event, x, y, flags, param):
    global selected_color
    if event == cv2.EVENT_LBUTTONDOWN:
        img = param
        selected_color = img[y, x].tolist()
        print(f"Color seleccionado: {selected_color} (R,G,B)")

# Función para nada, solo para crear sliders
def nothing(x):
    pass

# Cargar imagen para seleccionar color
img_selector = cv2.imread("C:/Users/Arcano/OneDrive/Escritorio/fotosjose/joseformal.jpg")  # Imagen para seleccionar el color
img_filter = cv2.imread("C:/Users/Arcano/OneDrive/Escritorio/fotosjose/joseformal.jpg")     # Imagen sobre la que aplicarás el filtro

cv2.namedWindow("Sliders")
cv2.createTrackbar("R Min", "Sliders", 0, 255, nothing)
cv2.createTrackbar("R Max", "Sliders", 255, 255, nothing)
cv2.createTrackbar("G Min", "Sliders", 0, 255, nothing)
cv2.createTrackbar("G Max", "Sliders", 255, 255, nothing)
cv2.createTrackbar("B Min", "Sliders", 0, 255, nothing)
cv2.createTrackbar("B Max", "Sliders", 255, 255, nothing)

cv2.imshow("Selecciona un color (clic izquierdo)", img_selector)
cv2.setMouseCallback("Selecciona un color (clic izquierdo)", select_color, img_selector)

print("Haz clic en la imagen para seleccionar un color.")

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC para salir
        break
    elif key == ord('q') and selected_color is not None:
        # Obtener valores de los sliders
        r_min = cv2.getTrackbarPos("R Min", "Sliders")
        r_max = cv2.getTrackbarPos("R Max", "Sliders")
        g_min = cv2.getTrackbarPos("G Min", "Sliders")
        g_max = cv2.getTrackbarPos("G Max", "Sliders")
        b_min = cv2.getTrackbarPos("B Min", "Sliders")
        b_max = cv2.getTrackbarPos("B Max", "Sliders")

        # Convertir imagen BGR a RGB para que coincida el orden
        img_rgb = cv2.cvtColor(img_filter, cv2.COLOR_BGR2RGB)

        # Crear máscaras
        lower_bound = np.array([r_min, g_min, b_min])
        upper_bound = np.array([r_max, g_max, b_max])
        mask = cv2.inRange(img_rgb, lower_bound, upper_bound)

        # Aplicar máscara
        result = cv2.bitwise_and(img_filter, img_filter, mask=mask)

        cv2.imshow("Resultado del filtro", result)

cv2.destroyAllWindows()