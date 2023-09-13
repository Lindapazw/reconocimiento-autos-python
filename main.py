import cv2

cars_cascade = cv2.CascadeClassifier('cars.xml')

cap = cv2.VideoCapture('autos.avi')  # Asegúrate de poner el nombre correcto del video

# Verificar si el clasificador se cargó correctamente
if cars_cascade.empty():
    print("Error: No se pudo cargar el clasificador.")
    exit()

# Verificar si el video se abrió correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir el archivo de video.")
    exit()

while True:
    ret, img = cap.read()

    # Verificar si se llegó al final del video
    if not ret:
        print("Fin del video.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cars = cars_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)

    # Esperar 1 milisegundo entre cuadros
    k = cv2.waitKey(1)

    if k == 27:  # 27 es el ascii para esc
        break

cap.release()
cv2.destroyAllWindows()