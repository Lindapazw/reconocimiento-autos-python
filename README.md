# Readme - Detección de Autos con OpenCV
Este código utiliza OpenCV, una biblioteca de visión por computadora, para detectar autos en un video. Asegúrate de tener OpenCV instalado en tu entorno de desarrollo antes de ejecutar este código.

## Requisitos Previos
 Python (versión recomendada: 3.x)
OpenCV (instalado con pip install opencv-python)
Archivo de clasificación cars.xml (este archivo debe estar presente en el mismo directorio que tu script)
## Cómo Usar
Instalación de Dependencias:

Antes de comenzar, asegúrate de tener Python y OpenCV instalados. Si no tienes OpenCV instalado, puedes instalarlo usando el siguiente comando:

## Copy code
`pip install opencv-python`
Archivo de Clasificación:

Asegúrate de tener el archivo cars.xml presente en el mismo directorio que tu script. Este archivo es necesario para el funcionamiento del clasificador de autos.

## Ejecución del Script:

Puedes ejecutar el script desde tu entorno de Python. Asegúrate de tener el video autos.avi presente en el mismo directorio que tu script o cambia la ruta del archivo de video en la línea:

python
Copy code
cap = cv2.VideoCapture('autos.avi')
Visualización:

Una vez que el script se ejecuta, se abrirá una ventana que mostrará el video con las detecciones de autos resaltadas.

Los autos detectados estarán rodeados por un rectángulo azul.
Presiona la tecla 'Esc' para salir del programa.

## Errores Comunes
Si experimentas errores relacionados con la carga del clasificador o la apertura del video, asegúrate de que los archivos `cars.xml` y `autos.avi` estén presentes en el mismo directorio que tu script, o proporciona las rutas correctas en el código.

## Notas Adicionales
Este código está configurado para terminar cuando se llega al final del video o cuando se presiona la tecla `Esc`.

Asegúrate de tener los permisos adecuados para acceder al archivo de video especificado.

Si encuentras algún problema o tienes sugerencias de mejora, no dudes en modificar el código o comunicarte con el autor del código.

¡Disfruta explorando la detección de autos con OpenCV!
