<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">Servicio web para la recomendación de playlists a partir de otra playlist</h1>

  <p align="center">
    TFG para el <a href="https://esiiab.uclm.es/grado/datos.php">Grado en Ingeniería Informática</a> de la <a href="https://www.uclm.es">Universidad de Castilla-La Mancha</a>
    <br />
    <br />
    <a href="docs/Memoria.pdf">Memoria del proyecto</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## Acerca del proyecto

### Resumen

Desde el auge de Internet y la aparición de los primeros reproductores de MP3, a finales de los años 90, el mundo de la música en formato digital ha ido evolucionando y  ganando protagonismo hasta tal punto que en 2014 superó en ingresos al formato físico.

Actualmente, mediante una suscripción a un servicio de música en streaming, tenemos acceso a más de 50 millones de canciones (este es el caso de _Spotify_). Ante un catálogo de música tan extenso, surge la necesidad de ayudar al usuario a descubrir o sugerir contenido acorde con sus gustos musicales, ya que este no puede dedicar todo su tiempo a buscar entre todo el contenido disponible. Aparte, la habilidad de búsqueda disminuye constantemente, ya que el contenido aumenta de forma significativa conforme pasan los años. Para solucionar este problema, se hace uso de los sistemas de recomendación. Su 
influencia, presencia e importancia han ido en aumento a lo largo del tiempo, ya que nos ayudan a filtrar contenido interminable.

Este proyecto tiene como objetivo construir un sistema para la creación o completado de playlists de canciones para el servicio de música en streaming _Spotify_. A partir de una playlist compuesta por un título y/o un conjunto inicial de canciones, nuestro sistema debe ser capaz de crear una lista desde cero (en el caso de que sólo se le proporcione el título) o completar una lista con canciones relacionadas a las facilitadas por 
el usuario y el título propuesto.

<br>

### Autoría
<u>Alumno</u>:
* Miguel Ángel Cantero Víllora

<u>Tutores</u>:
* José Antonio Gámez Martín
* Juan Ángel Aledo Sánchez

<br>

## Tecnologías empleadas

### Lenguajes
* __Python__: Ciencia de datos y servicio web
* __HTML__ y __C#__: Aplicación web 

<br>

### Herramientas de desarrollo 
* __Jupyter Notebook__: Entorno de programación interactivo, mediante el cual podemos introducir texto en formato _markdown_ junto a código _Python_ haciendo uso de los _notebooks_ o libretas.
* __Visual Studio Code__: Conocido editor de código de _Microsoft_, el cual ha sido empleado a la hora de visualizar los archivos creados para almacenar los datos, tanto en formato _CSV_ como _JSON_, para el desarrollo de scripts empleados para ejecutar los procesos relacionados con la recopilación de datos y el entrenamiento del modelo, y para desarrollar la aplicación web y la _API REST_.

<br>

### Bibliotecas
* __Spotipy__: Biblioteca de Python para usar la WebAPI de Spotify.
* __Numpy__: Ofrece mayor soporte a vectores y matrices, constituyendo una biblioteca de funciones matemáticas de alto nivel para operar con estos elementos.
* __Pandas__: Es una biblioteca de código abierto para Python que proporciona estructuras de datos y herramientas de análisis de alto rendimiento y fáciles de emplear.
* __NLTK__: Este toolkit es una de las bibliotecas más potentes para procesamiento del lenguaje natural.
* __SciPy__: Biblioteca de código abierto basada en Python, que se utiliza en matemáticas,
ciencia e ingeniería.
* __Scikit-Learn__: Biblioteca empleada para problemas de aprendizaje automático o machine learning.
* __LightFM__: Es una biblioteca que contiene numerosos algoritmos utilizados en los sistemas de recomendación. 
