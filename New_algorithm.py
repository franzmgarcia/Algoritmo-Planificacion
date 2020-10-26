#! /usr/bin/env python
import time # usamos la libreria time para poder medir el tiempo de ejecucion del programa
import numpy as np
import pandas as pd

"""
        En este caso tenemos un algoritmo greedy que resuelve solo algunos mapas 
        La idea es que ya conocemos la posicion final
        Si estamos inicialmente en X en una posicion menor (vease mapa 1, x = 2) a la posicion final (mapa 1, x = 7)
        Lo que buscaremos es aumentar siempre nuestra posicion en x hasta que llegamos a esa posicion final en x
        Si encontramos alguna pared buscaremos ir hacia la derecha siempre para esquivar los obstaculos
        Si por algun motivo ir hacia la derecha tambien es un problema, damos la oportunidad de ir hacia la izquierda una vez
        Con estos movimientos hacia la izquierda o derecha no se cambia el objetivo inicial que es siempre aumentar nuestra posicion en x
        Lo que se agrega para que no se quede tan estancado el algoritmo, es el uso de los nodos visitados cuando vamos hacia la derecha
        Si ir hacia la derecha no es una solucion, iremos una vez hacia la izquierda (en caso de que sea posible)
        La proxima vez que tratemos de ir hacia la derecha nos encontraremos con un nodo visitado por lo que iremos hacia la izquierda
        Asi varias veces hasta que lleguemos a un punto en el que podamos ir hacia abajo y lleguemos a la misma coordenada en x
        Una vez llegado a ese punto vamos hacia la izquierda como primera opcion, y si no es posible volvemos a hacer el barrido 
        Como se realizo previamente

        Este algoritmo adicionalmente mide el tiempo de ejecucion
"""

start_time = time.time()

"""
############ Mapa 1 ###################
FILE_NAME = "map1.csv"
START_X = 2
START_Y = 2
END_X = 7
END_Y = 2
########################################
"""

"""
# Descomentar para probar el mapa 2
FILE_NAME = "map2.csv"
START_X = 2
START_Y = 2
END_X = 10
END_Y = 7
"""


# Descomentar para probar el mapa 6
FILE_NAME = "map6.csv"
START_X = 2
START_Y = 2
END_X = 10
END_Y = 17


# Definimos la clase nodo que tiene las posiciones en x,y, su propio id y un nodo padre
# Este tiene un metodo dump definido que imprime todos estos valores
class Node:
    def __init__(self, x, y, myId, parentId):
        self.x = x
        self.y = y
        self.myId = myId
        self.parentId = parentId
    def dump(self):
        print("---------- x "+str(self.x)+\
                         " | y "+str(self.y)+\
                         " | id "+str(self.myId)+\
                         " | parentId "+str(self.parentId))

# Definimos el arreglo nodes, que sera utilizado para poder conocer los nodos recorridos
nodes = []

# Hacemos un nodo de inicio, usando la clase Node, con las posiciones de inicio en x e y 
# que fueron inicializadas al inicio del programa
# Finalmente el id de este nodo sera 0, ya que es el primer nodo y le damos el valor -2
# como parentId, de manera que sirva como identificador de que este fue el nodo de inicio
init = Node(START_X, START_Y, 0, -2)
# init.dump()

# anadimos el nodo al arreglo nodes usando append
nodes.append(init)

# el charmap es el mapa en el que se va a realizar el recorrido
# para esto tendremos 5 tipos de valores posibles para cada nodo
# 0: libre
# 1: ocupado
# 2: visitado
# 3: inicio
# 4: fin
charMap = []

# hacemos la funcion dumpMap para cargar el mapa en el charMap
def dumpMap():
    for line in charMap:
        print(line)
# para esto primero abrimos el archivo csv y leemos cada linea
with open(FILE_NAME) as f:
    line = f.readline()
    while line:
        charLine = line.strip().split(',')
        charMap.append(charLine)
        line = f.readline()
# anadimos al final los nodos de inicio y de fin, es decir
# suponemos que ya conocemos nuestra posicion de inicio y la que queremos que sea la posicion final

charMap[START_X][START_Y] = '3'
charMap[END_X][END_Y] = '4'

# usamos la funcion dumpMap y cargamos en charMap
dumpMap()

done = False
goalParentId = -1

# Hacemos un loop infinito, hasta que se encuentre la solucion al problema
# Nota: no es la mejor opcion. Podriamos indicar un numero de iteraciones y si para ese momento no encontramos una solucion
# salimos del loop e indicamos que no tenemos una solucion. Podria ser
while not done:
    print("--------------------- number of nodes: "+str(len(nodes)))
    for node in nodes:

        node.dump()
        # Si el valor de x+1 del nodo actual es menor que el valor de la coordenada final de x vamos abajo 
        if ((node.x+1)<=END_X):
            tmpX = node.x +1
            tmpY = node.y
            # Si llegamos a la meta, es decir la posicion 4, indicamos que llegamos y el nuevo goalParentId es el Id del nodo
            # en el que estas antes de moverte, y salimos del loop con un break
            if( charMap[tmpX][tmpY] == '4' ):
                print("Abajo: Llegamos")
                goalParentId = node.myId
                done = True
                break
            # Si encontramos un espacio vacio nos movemos y marcamos el nodo como visitado
            # indicando el nodo en el charmap como 2 y añadiendo el nuevo nodo al arreglo
            elif( charMap[tmpX][tmpY] == '0'):
                print("Abajo: nodo visitado")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)

            # Si encontramos un obstaculo vamos a intentar movernos a la derecha, reescribimos tmpX y tmpY 
            # para hacer esto        
            elif( charMap[tmpX][tmpY] == '1'):

                tmpX = node.x
                tmpY = node.y + 1

                # hacemos las mismas comprobaciones que cuando nos movemos para abajo
                if( charMap[tmpX][tmpY] == '4'):
                    print("Derecha: Llegamos")
                    goalParentId = node.myId
                    done = True
                    break
                elif( charMap[tmpX][tmpY] == '0'):
                    print("Derecha: nodo visitado")
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY]='2'
                    nodes.append(newNode)
                # Hasta esta, en la que verificamos si el nodo ya fue visitado
                # Esto sirve un poco de via de escape para el algoritmo, de manera que pueda salir de estancamientos
                # cuando al avanzara vayamos todo hacia la derecha
                # Si encontramos que el nodo que ibamos a visitar ya habia sido visitado, nos movemos a la izquierda
                elif( charMap[tmpX][tmpY] == '2' and charMap[node.x][node.y -1] != '1'):
                    tmpX = node.x
                    tmpY = node.y -1
                    print("Izquierda: porque ya antes ha sido visitado")
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)    
                elif( charMap[tmpX][tmpY] == '1'):
                    
                    #Si nos encontramos con que es un obstaculo, intentaremos ir hacia la izquierda

                    tmpX = node.x
                    tmpY = node.y - 1

                    # aca solo verificamos las condiciones de cuando nos movemos hacia abajo, y de la misma manera
                    if( charMap[tmpX][tmpY] == '4'):
                        print("Izquierda: Llegamos")
                        goalParentId = node.myId
                        done = True
                        break
                    elif( charMap[tmpX][tmpY] == '0'):
                        print("Izquierda: nodo visitado")
                        newNode = Node(tmpX, tmpY,len(nodes), node.myId)
                        charMap[tmpX][tmpY]='2'
                        nodes.append(newNode)

        # Finalmente cuando llegamos a la misma posicion en la coordenada x, del punto final del recorrido
        # hacemos un barrido hacia la izquierda (esto se hizo asi, inspirado en tratar de resolver, al menos, el mapa 1)
        # haciendolo de esta manera la ejecucion es mucho mas rapida que usando un algoritmo bfs        
        if ((node.x) == END_X):
            
            # nos movemos hacia la izquierda, si encontramos el 
            tmpX = node.x
            tmpY = node.y -1
            if( charMap[tmpX][tmpY] == '4' ):
                print("Izquierda: Llegamos")
                goalParentId = node.myId
                done = True
                break
            elif( charMap[tmpX][tmpY] == '0'):
                print("Izquierda: nodo visitado")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
            # A fin de poder solucionar mas mapas agregamos la misma condicion de visitado que teniamos anteriormente
            # solo que en este caso el movimiento es hacia la derecha
            elif( charMap[tmpX][tmpY] == '2'):
                tmpY = node.y + 1
                if ( charMap[tmpX][tmpY]=='4'):
                    print("Derecha: Llegamos")
                    goalParentId = node.myId
                    done = True
                    break
                else:
                    print("Derecha: porque antes ya ha sido visitado")
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)
            # Y esta es la condicion que nos permite salirnos al menos una vez del estancamiento del algoritmo
            # y entrar al menos una vez en la condicion igual a 2
            elif( charMap[tmpX][tmpY] == '1'):
                tmpY = node.y + 1
                print("Obstaculo a la izquierda vamos a la derecha")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)


        # Volcamos el mapa nuevo despues de cada iteracion
        dumpMap()

print("%%%%%%%%%%%%%%%%%%%")
ok = False

# y aca tenemos otro loop infinito que hace un recuento de los puntos por donde se hizo el recorrido antes de llegar a la meta
# la clave es que eso se sigue haciendo hasta que llegamos a nuestro nodo de inicio que tiene de parentId -2, solo un nodo tiene
# de parentId este numero, por lo que sabemos que ese sera nuestro nodo de partida
while not ok:
    for node in nodes:
        if( node.myId == goalParentId ):
            node.dump()
            goalParentId = node.parentId
            if( goalParentId == -2):
                print("%%%%%%%%%%%%%%%%%2")
                ok = True

t_ejecucion = time.time() - start_time
print("Tiempo de ejecucion: "+ str(t_ejecucion)+" segundos")

array_csv = np.asarray(charMap)
print(array_csv)
pd.DataFrame(array_csv).to_csv("solve"+FILE_NAME,header=None,index=None)