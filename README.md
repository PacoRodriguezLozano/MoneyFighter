# MoneyFighter
Los deportes de contacto, y sobre todo las MMA, son un deporte muy variado con una gran diversidad de estilos de pelea, técnicas y estrategias muy diferentes, dando lugar a resultados, a veces, sorprendentes. Sin embargo, el objetivo de este proyecto es determinar la influencia del estilo del peleador y su rival en el resultado de una pelea usando las estadísticas de golpeo y grappling de ellos.
Los objetivos de este proyecto son los siguientes:
* Crear un modelo de predicción del ganador de una pelea de MMA lo más fiable posible que la probabilidad inicial del 50%
* Evaluar si es posible elaborar un modelo de predicción del resultado de una pelea de MMA teniendo en cuenta tan solo las cualidades técnicas y físicas de ambos peleadores

# Resultados obtenidos
Modelo de predicción del ganador con un 68% de aciertos

# Obtención de los datos (Si no quieres repetir el Web Scraping)
1. Enlace a los datos obtenidos mediante Web Scraping a fecha de 05/02/2023:
https://drive.google.com/drive/folders/1kdoIGkDWWuYlr_DpAqAgxts2cf0cZfss?usp=share_link 
2. Introduce el archivo en la carpeta donde hayas clonado el repositorio

#  Instrucciones para replicar el proyecto
1. Clonar el proyecto a tu repositorio local. Enlace: 

https://github.com/PacoRodriguezLozano/MoneyFighter 

2. Instalar las librerías necesarias especificadas en el archivo “Requirement.txt”.

3. Si quieres realizar de nuevo la adquisición de los datos debes ejecutar todos los notebooks en el siguiente orden:

* Data_wangling.ipynb
* Modelo_predictivo.ipynb
* Frontend.ipnb
Ten en cuenta que cambios en la estructura de las páginas que se utilizaron para obtener los datos o cambios en su código podrían resultar en un error en el notebook. Además, si se introducen nuevas barreras para evitar el WebSraping puede que se produzca un error. 
Durante el desarrollo del proyecto, tan solo se encontró el problema de limitación de las solicitudes del servidor que se solucionó incorporando una gestión del error y un tiempo de pausa usando la librería “time”.  
4. Si prefieres usar los datos que se obtuvieron en el momento del desarrollo del proyecto (datos actualizados hasta 05/02/2023):
* Descargar datasets obtenidos tras el Web Scraping del siguiente link: https://drive.google.com/drive/folders/1kdoIGkDWWuYlr_DpAqAgxts2cf0cZfss?usp=share_link . Y colocarlos en la misma carpeta en la que clonaste el proyecto.
* Correr los notebooks en el mismo orden que antes, pero comenzando por el apartado 1.1 y 2.1 saltando así la parte de adquisición de los datos.

