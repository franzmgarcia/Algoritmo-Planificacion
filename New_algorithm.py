#! /usr/bin/env python


############ Mapa 1 ###################
FILE_NAME = "map1.csv"
START_X = 2
START_Y = 2
END_X = 7
END_Y = 2
########################################

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

nodes = []

init = Node(START_X, START_Y, 0, -2)
# init.dump()

nodes.append(init)

charMap = []

def dumpMap():
    for line in charMap:
        print(line)

with open(FILE_NAME) as f:
    line = f.readline()
    while line:
        charLine = line.strip().split(',')
        charMap.append(charLine)
        line = f.readline()

charMap[START_X][START_Y] = '3'
charMap[END_X][END_Y] = '4'

dumpMap()

done = False
goalParentId = -1

while not done:
    print("--------------------- number of nodes: "+str(len(nodes)))
    for node in nodes:
        node.dump()
        # Verificamos si estamos por debajo de la x final, y trataremos de bajar hasta el nivel de x  
        if ((node.x+1)<=END_X):
            tmpX = node.x +1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif( charMap[tmpX][tmpY] == '0'):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
            elif( charMap[tmpX][tmpY] == '1'):

                tmpX = node.x
                tmpY = node.y + 1
                if( charMap[tmpX][tmpY] == '4'):
                    print("up: GOAL_V2")
                    goalParentId = node.myId
                    done = True
                    break
                elif( charMap[tmpX][tmpY] == '0'):
                    print("first down, now right")
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY]='2'
                    nodes.append(newNode)
                elif( charMap[tmpX][tmpY] == '2'):
                    tmpX = node.x
                    tmpY = node.y -1
                    print("left because was previously visited")
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)    
                elif( charMap[tmpX][tmpY] == '1'):
                    
                    tmpX = node.x
                    tmpY = node.y - 1
                    if( charMap[tmpX][tmpY] == '4'):
                        print("up:GOAL_V2")
                        goalParentId = node.myId
                        done = True
                        break
                    elif( charMap[tmpX][tmpY] == '0'):
                        print("first down, now left")
                        newNode = Node(tmpX, tmpY,len(nodes), node.myId)
                        charMap[tmpX][tmpY]='2'
                        nodes.append(newNode)

        
        if ((node.x) == END_X):

            tmpX = node.x
            tmpY = node.y -1
            if( charMap[tmpX][tmpY] == '4' ):
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif( charMap[tmpX][tmpY] == '0'):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
            elif( charMap[tmpX][tmpY] == '2'):
                tmpY = node.y + 1
                if ( charMap[tmpX][tmpY]=='4'):
                    print("up: GOALL M")
                    goalParentId = node.myId
                    done = True
                    break
                else:
                    print("right because was previously visited")
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)
            elif( charMap[tmpX][tmpY] == '1'):
                tmpY = node.y + 1
                print("obstacle in right, now go to the left")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)


        
        dumpMap()

print("%%%%%%%%%%%%%%%%%%%")
ok = False
while not ok:
    for node in nodes:
        if( node.myId == goalParentId ):
            node.dump()
            goalParentId = node.parentId
            if( goalParentId == -2):
                print("%%%%%%%%%%%%%%%%%2")
                ok = True
