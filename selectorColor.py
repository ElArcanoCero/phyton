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
        print(f"Color seleccionado: {selected_color[2]} (R,G,B)")
        cv2.namedWindow("Sliders")
        # faltan filtros para overload tambien debes convertit selected_color a variables para uarlo  en la mascara 
        # y en la creacion de los sliders
        cv2.createTrackbar("R Min", "Sliders", selected_color[0]-20, 255, slider)
        cv2.createTrackbar("R Max", "Sliders", selected_color[0]+20, 255, slider)
        cv2.createTrackbar("G Min", "Sliders", selected_color[1]-20, 255, slider)
        cv2.createTrackbar("G Max", "Sliders", selected_color[1]+20, 255, slider)
        cv2.createTrackbar("B Min", "Sliders", selected_color[2]-20, 255, slider)
        cv2.createTrackbar("B Max", "Sliders", selected_color[2]+20, 255, slider)

# Función para nada, solo para crear sliders
def slider(x):
    pass

# Cargar imagen para seleccionar color
img_selector = cv2.imread("C:/Users/Arcano/OneDrive/Escritorio/fotosjose/joseformal.jpg")  # Imagen para seleccionar el color
img_filter = cv2.imread("C:/Users/Arcano/OneDrive/Escritorio/fotosjose/joseformal.jpg")     # Imagen sobre la que aplicarás el filtro



cv2.imshow("Selecciona un color (clic izquierdo)", img_selector)
cv2.setMouseCallback("Selecciona un color (clic izquierdo)", select_color, img_selector)

print("Haz clic en la imagen para seleccionar un color.")

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC para salir
        break
    elif key == ord('q') and selected_color is not None:
        # Obtener valores de los sliders
        r_min = selected_color[0]-20
        r_max = selected_color[0]+20
        g_min = selected_color[1]-20
        g_max = selected_color[1]+20
        b_min = selected_color[2]-20
        b_max = selected_color[2]+20

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