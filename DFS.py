import numpy as np
from PIL import Image



class Move:
    def __init__(self,coordinate,parent):
        self.coordinate = coordinate
        self.parent = parent

def findStartEnd(img):
    start = (254,0,0)
    end = (0,9,254)
    array = np.array(img)

    Xs,Ys = np.where(np.all(array == start,axis=2))
    Xe,Ye = np.where(np.all(array == end, axis=2))

    startLoc = (Xs[0], Ys[0])
    endLoc = (Xe[0], Ye[0])

    return startLoc, endLoc

def search(start,end,pix,img):
    openStack = []
    visited = []
    isFound = False
    array = np.array(img)
    openStack.append(Move(start,(-1,-1)))
    contains = False

    while isFound == False:

        currentMove = openStack[len(openStack)-1]
        if(currentMove.coordinate != start):
            array[currentMove.coordinate[0], currentMove.coordinate[1]] = (255, 255, 0)

        openStack.pop(len(openStack)-1)
        visited.append(currentMove)
        surroundings = [Move((currentMove.coordinate[0], currentMove.coordinate[1] - 1),currentMove.coordinate),
                        Move((currentMove.coordinate[0] + 1, currentMove.coordinate[1]),currentMove.coordinate),
                        Move((currentMove.coordinate[0], currentMove.coordinate[1] + 1),currentMove.coordinate),
                        Move((currentMove.coordinate[0] - 1, currentMove.coordinate[1]),currentMove.coordinate)
                        ]
        for move in surroundings:
            if(end == move.coordinate):
                isFound = True

            if ((pix[move.coordinate[1],move.coordinate[0]] >= (220, 220, 220)) and pix[move.coordinate[1],move.coordinate[0]] != (255, 255, 0) and move.coordinate != start ):
                for i in visited:
                    if(i.coordinate == move.coordinate):
                        contains = True
                if(contains == False):
                    openStack.append(move)
                contains = False

    path = []
    path.append(visited[len(visited)-1])
    array[path[0].coordinate[0],path[0].coordinate[1]] = (0,255,0)
    for x in visited[len(visited)-2:0:-1]:
        if(x.coordinate == path[len(path)-1].parent):
            path.append(x)
            array[x.coordinate[0],x.coordinate[1]] = (0,255,0)
    img = Image.fromarray(array)
    img.save('solution.png')

    return path

#Labirintus megadás
img = Image.open("maze7.png")
pix = img.load()

start,end = findStartEnd(img)
path = search(start,end,pix,img)

for x in path:
    print(x.coordinate)
