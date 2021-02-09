# Algoritmo Planificacion de trayectoria

## Implementación

- Python 3.6.8

Librerías:

- Time
- Numpy
- Pandas

## Introducción

Esta actividad consistió en la elaboración de un algoritmo "greedy" de planificación de trayectoria. En este caso en particular se utilizó el lenguaje de programación Python y se utilizó como código base, un código previamente dado para realizar planificación de trayectorias usando la técnica Breadth First Search, transformando su funcionamiento hasta que el mismo se convirtió en un código greedy capaz de ir de un punto a otro para algunos mapas. En este caso, se añade en el repositorio 3 mapas en formato .csv de los cuales se puede comprobar su correcto funcionamiento con condiciones previas de inicio y fin, y otros 3 archivos .csv con la correspondiente solución que es generada automaticamente por el programa. Se incluye además, el código previamente dado, correspondiente al archivo [main.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/main.py), el código de funcionamiento nuevo en el que además se puede determinar el tiempo de ejecución [New_algorithm.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm.py) y por último, el mismo código con funcionamiento greedy en el que se permite al usuario indicar por teclado la posición final para la trayectoria, [New_algorithm_input.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm_input.py).

## Funcionamiento

El algoritmo creado [New_algorithm.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm.py) y [New_algorithm_input.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm_input.py) corresponde a un algoritmo greedy que no funciona correctamente en todos los mapas y su funcionamiento se ve limitado a algunas condiciones. Estos mapas como se mencionó anteriormente vienen en formatos .csv y están dados, tal que cada punto dentro del mapa posee un número que lo describe de una manera diferente, siendo los números y sus descripciones las siguientes:

- 0: nodo libre
- 1: nodo ocupado
- 2: nodo visitado
- 3: nodo inicio
- 4: nodo final

El algoritmo posee una clase nodos, en los que se señala la posición en x e y en el mapa, así como un identificador de Id y un identificador del nodo padre, que indica cual fue el paso previo para llegar al nodo en el que nos encontramos en el recorrido. Estos nodos recorridos son añadidos en cada uno de los pasos que se dan durante el recorrido, teniendo al final un arreglo de nodos. De esta manera, usando una estructura de tipo árbol, podemos volver en cada uno de los nodos una vez encontrado el nodo meta, para así reconstruir nuestro camino desde el inicio. 

Para llegar a la meta, el algoritmo busca realizar desplazamientos en la coordenada x, suponiendo que esta se encuentra por debajo de la posición final (esta es una de las condiciones para el correcto funcionamiento del programa), que ya se tiene como conocida. Si encontramos algún obstáculo, en nuestro camino hacia abajo, el programa está diseñado para intentar realizar movimientos a la derecha o a la izquierda (privilegiando el comportamiento del movimiento hacia la derecha) pero sin cambiar el planteamiento inicial de intentar siempre movimientos hacia abajo. El programa tiene además una manera de salir de huecos cuando realiza movimientos hacia la derecha, implementando movimientos hacia la izquierda cuando encontramos algún nodo ya visitado. Una vez se logra alcanzar la misma posición en x que la posición meta, se trata de realizar un barrido para la coordenada y, privilegiando en este caso los movimientos hacia la izquierda y dando vuelta en caso de encontrar algún obstáculo en el camino. Esto se hizo así, ya que en principio se trató de resolver el problema de encontrar una solución para el mapa 1, y después se hizo un poco más complejo, de manera que pudiera dar respuesta también a los mapas 2 y 6, por ejemplo.

## Resultados

Al ejecutar el programa, una de las cosas que podemos determinar para [New_algorithm.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm.py) es el tiempo de ejecución del programa y para eso hacemos uso de la librería time. Este tiempo de ejecución no fue medido para el archivo [New_algorithm_input.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm_input.py) ya que este nos permite señalar para el programa las coordenadas en x e y de la posición final que se quiere, y el punto de incluirlo en el otro archivo era hacer una comparación entre usar el algoritmo bfs del archivo [main.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/main.py) y el algoritmo greedy creado.

Otra de las cosas que fueron añadidas, es la posibilidad de generar un archivo automaticamente en formato .csv en función del mapa analizado, con la trayectoria seguida por el algoritmo desde el inicio hasta la meta. Estas soluciones se pueden ver en los archivos [solvemap1.csv](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/solvemap1.csv), [solvemap2.csv](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/solvemap2.csv) y [solvemap6.csv](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/solvemap6.csv), dadas las condiciones establecidas inicialmente en la actividad.

## Conclusiones y limitaciones 

El algoritmo creado sirve para determinar una ruta para ir desde un punto a otro, atravesando una serie de obstáculos. Aunque es cierto que posee algunas limitaciones evidentes de funcionamiento, como el hecho de que es un algoritmo que busca siempre desplazarse en una dirección en la coordenada x, y no posee la capacidad de dar vuelta en esta coordenada, también es cierto que para determinados problemas su funcionamiento puede ser mucho más rápido respecto a algoritmos de búsqueda exhaustiva como el BFS, que serían capaces de encontrar solución a cualquier problema dada su naturaleza para realizar la planificación.

En este sentido, para el algoritmo BFS tenemos un tiempo de ejecución cercano a los 0.1 segundos para el mapa 1 mientras que para el algoritmo greedy desarrollado, el tiempo de ejecución va hacia menos de la mitad, cercano a los 0.04 segundos. Para el mapa 2, algo más complejo, con el algoritmo BFS tenemos cerca de 0.25 segundos de tiempo de ejecución, mientras que con el algoritmo greedy el tiempo de ejecución es menor, de 0.17 segundos. Finalmente para el mapa 6, el más complejo de los 3 analizados, con el algoritmo BFS tenemos cerca de 0.716 segundos, mientras que para el algoritmo greedy el tiempo de ejecución es de 0.585 segundos. De acá que conseguimos un algoritmo que funciona más rápido para distintos casos, a pesar de tener sus limitaciones.

Adicionalmente, y como ya se ha indicado, se pueden observar distintas soluciones para los mapas 1,2 y 6 utilizando el archivo [New_algorithm_input.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm_input.py)

***

# Path Planning Algorithm

## Implementation

- Python 3.6.8

Libraries:

- Time
- Numpy
- Pandas

## Introduction

This activity consist in the creation of an greedy algorithm of path planning. In this particular case, it was used the programming language Python and a gave base code 

## Introducción

Esta actividad consistió en la elaboración de un algoritmo "greedy" de planificación de trayectoria. En este caso en particular se utilizó el lenguaje de programación Python y se utilizó como código base, un código previamente dado para realizar planificación de trayectorias usando la técnica Breadth First Search, transformando su funcionamiento hasta que el mismo se convirtió en un código greedy capaz de ir de un punto a otro para algunos mapas. En este caso, se añade en el repositorio 3 mapas en formato .csv de los cuales se puede comprobar su correcto funcionamiento con condiciones previas de inicio y fin, y otros 3 archivos .csv con la correspondiente solución que es generada automaticamente por el programa. Se incluye además, el código previamente dado, correspondiente al archivo [main.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/main.py), el código de funcionamiento nuevo en el que además se puede determinar el tiempo de ejecución [New_algorithm.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm.py) y por último, el mismo código con funcionamiento greedy en el que se permite al usuario indicar por teclado la posición final para la trayectoria, [New_algorithm_input.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm_input.py).

## Funcionamiento

El algoritmo creado [New_algorithm.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm.py) y [New_algorithm_input.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm_input.py) corresponde a un algoritmo greedy que no funciona correctamente en todos los mapas y su funcionamiento se ve limitado a algunas condiciones. Estos mapas como se mencionó anteriormente vienen en formatos .csv y están dados, tal que cada punto dentro del mapa posee un número que lo describe de una manera diferente, siendo los números y sus descripciones las siguientes:

- 0: nodo libre
- 1: nodo ocupado
- 2: nodo visitado
- 3: nodo inicio
- 4: nodo final

El algoritmo posee una clase nodos, en los que se señala la posición en x e y en el mapa, así como un identificador de Id y un identificador del nodo padre, que indica cual fue el paso previo para llegar al nodo en el que nos encontramos en el recorrido. Estos nodos recorridos son añadidos en cada uno de los pasos que se dan durante el recorrido, teniendo al final un arreglo de nodos. De esta manera, usando una estructura de tipo árbol, podemos volver en cada uno de los nodos una vez encontrado el nodo meta, para así reconstruir nuestro camino desde el inicio. 

Para llegar a la meta, el algoritmo busca realizar desplazamientos en la coordenada x, suponiendo que esta se encuentra por debajo de la posición final (esta es una de las condiciones para el correcto funcionamiento del programa), que ya se tiene como conocida. Si encontramos algún obstáculo, en nuestro camino hacia abajo, el programa está diseñado para intentar realizar movimientos a la derecha o a la izquierda (privilegiando el comportamiento del movimiento hacia la derecha) pero sin cambiar el planteamiento inicial de intentar siempre movimientos hacia abajo. El programa tiene además una manera de salir de huecos cuando realiza movimientos hacia la derecha, implementando movimientos hacia la izquierda cuando encontramos algún nodo ya visitado. Una vez se logra alcanzar la misma posición en x que la posición meta, se trata de realizar un barrido para la coordenada y, privilegiando en este caso los movimientos hacia la izquierda y dando vuelta en caso de encontrar algún obstáculo en el camino. Esto se hizo así, ya que en principio se trató de resolver el problema de encontrar una solución para el mapa 1, y después se hizo un poco más complejo, de manera que pudiera dar respuesta también a los mapas 2 y 6, por ejemplo.

## Resultados

Al ejecutar el programa, una de las cosas que podemos determinar para [New_algorithm.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm.py) es el tiempo de ejecución del programa y para eso hacemos uso de la librería time. Este tiempo de ejecución no fue medido para el archivo [New_algorithm_input.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm_input.py) ya que este nos permite señalar para el programa las coordenadas en x e y de la posición final que se quiere, y el punto de incluirlo en el otro archivo era hacer una comparación entre usar el algoritmo bfs del archivo [main.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/main.py) y el algoritmo greedy creado.

Otra de las cosas que fueron añadidas, es la posibilidad de generar un archivo automaticamente en formato .csv en función del mapa analizado, con la trayectoria seguida por el algoritmo desde el inicio hasta la meta. Estas soluciones se pueden ver en los archivos [solvemap1.csv](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/solvemap1.csv), [solvemap2.csv](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/solvemap2.csv) y [solvemap6.csv](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/solvemap6.csv), dadas las condiciones establecidas inicialmente en la actividad.

## Conclusiones y limitaciones 

El algoritmo creado sirve para determinar una ruta para ir desde un punto a otro, atravesando una serie de obstáculos. Aunque es cierto que posee algunas limitaciones evidentes de funcionamiento, como el hecho de que es un algoritmo que busca siempre desplazarse en una dirección en la coordenada x, y no posee la capacidad de dar vuelta en esta coordenada, también es cierto que para determinados problemas su funcionamiento puede ser mucho más rápido respecto a algoritmos de búsqueda exhaustiva como el BFS, que serían capaces de encontrar solución a cualquier problema dada su naturaleza para realizar la planificación.

En este sentido, para el algoritmo BFS tenemos un tiempo de ejecución cercano a los 0.1 segundos para el mapa 1 mientras que para el algoritmo greedy desarrollado, el tiempo de ejecución va hacia menos de la mitad, cercano a los 0.04 segundos. Para el mapa 2, algo más complejo, con el algoritmo BFS tenemos cerca de 0.25 segundos de tiempo de ejecución, mientras que con el algoritmo greedy el tiempo de ejecución es menor, de 0.17 segundos. Finalmente para el mapa 6, el más complejo de los 3 analizados, con el algoritmo BFS tenemos cerca de 0.716 segundos, mientras que para el algoritmo greedy el tiempo de ejecución es de 0.585 segundos. De acá que conseguimos un algoritmo que funciona más rápido para distintos casos, a pesar de tener sus limitaciones.

Adicionalmente, y como ya se ha indicado, se pueden observar distintas soluciones para los mapas 1,2 y 6 utilizando el archivo [New_algorithm_input.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm_input.py)













