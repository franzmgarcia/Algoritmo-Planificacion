# Algoritmo Planificacion de trayectoria

## Introducción

Esta actividad consistió en la elaboración de un algoritmo "greedy" de planificación de trayectoria. En este caso en particular se utilizó el lenguaje de programación Python y se utilizó como código base, un código previamente dado para realizar planificación de trayectorias usando la técnica Breadth First Search, transformando su funcionamiento hasta que el mismo se convirtió en un código greedy capaz de ir de un punto a otro para algunos mapas. En este caso, se añade en el repositorio 3 mapas en formato .csv de los cuales se puede comprobar su correcto funcionamiento con condiciones previas de inicio y fin. Se incluye además, el código previamente dado, correspondiente al archivo [main.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/main.py), el código de funcionamiento nuevo en el que además se puede determinar el tiempo de ejecución [New_algorithm.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm.py) y por último, el mismo código con funcionamiento greedy en el que se permite al usuario indicar la posición final para la trayectoria, [New_algorithm_input.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm_input.py).

## Funcionamiento

El algoritmo creado [New_algorithm.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm.py) y [New_algorithm_input.py](https://github.com/franzmgarcia/Algoritmo-Planificacion/blob/master/New_algorithm_input.py) corresponde a un algoritmo greedy que no funciona correctamente en todos los mapas y su funcionamiento se ve limitado a algunas condiciones. Estos mapas como se mencionó anteriormente vienen en formatos .csv y están dados, tal que cada punto dentro del mapa posee un número que lo describe de una manera diferente, siendo los números y sus descripciones las siguientes:

- 0: nodo libre
- 1: nodo ocupado
- 2: nodo visitado
- 3: nodo inicio
- 4: nodo final

El algoritmo posee una clase nodos, en los que se señala la posición en x e y en el mapa, así como un identificador de Id y un identificador del nodo padre, que indica cual fue el paso previo para llegar al nodo en el que nos encontramos en el recorrido. Estos nodos recorridos son añadidos en cada uno de los pasos que se dan durante el recorrido, teniendo al final un arreglo de nodos. De esta manera, usando una estructura de tipo árbol, podemos volver en cada uno de los nodos una vez encontrado el nodo meta, para así reconstruir nuestro camino desde el inicio. 

Para llegar a la meta, el algoritmo busca realizar desplazamientos en la coordenada x, suponiendo que esta se encuentra por debajo de la posición final (esta es una de las condiciones para el correcto funcionamiento del programa), que ya se tiene como conocida. Si encontramos algún obstáculo, en nuestro camino hacia abajo, el programa está diseñado para intentar realizar movimientos a la derecha o a la izquierda (privilegiando el comportamiento del movimiento hacia la derecha) pero sin cambiar el planteamiento inicial de intentar siempre movimientos hacia abajo. El programa tiene además una manera de salir de huecos cuando realiza movimientos hacia la derecha, implementando movimientos hacia la izquierda cuando encontramos algún nodo ya visitado. Una vez se logra alcanzar la misma posición en x que la posición meta, se trata de realizar un barrido para la coordenada y.
