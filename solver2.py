import numpy as np
import random
from PIL import Image



img = Image.open("maze2.png")
pix = img.load()

class Move:
    def __init__(self,move,parent):
        self.move = move
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


start, end = findStartEnd(img)
print(str(start))
print(str(end))

def search(start,end,pix,img):
    openStack = []
    visited = []
    isFound = False
    array = np.array(img)
    openStack.append(start)

    while isFound == False:



        current = openStack[len(openStack)-1]
        array[current[1], current[0]] = (255, 255, 0)
        img = Image.fromarray(array)
        openStack.pop(len(openStack)-1)
        visited.append(current)
        surroundings = [(current[0], current[1] - 1),   #KI kell egészíteni egy Listával amelyben lehet tárolni az utovalat VAGY a surroundingsbol/movebol rekordot kell készíteni és tárolni kell az ősöket
                        (current[0] + 1, current[1]),
                        (current[0], current[1] + 1),
                        (current[0] - 1, current[1])
                        ]
        for move in surroundings:
            if(end == move):
                openStack.append(move)
                isFound = True

            if ((pix[move] >= (220, 220, 220)) and pix[move] != (255, 255, 0) and move != start and move not in visited):
                openStack.append(move)

        for p in openStack[:-1]:
            array[p[1], p[0]] = (0, 255, 0)
        img = Image.fromarray(array)
        img.save('solution.png')

    return openStack


img = Image.open("maze2.png")
pix = img.load()

start,end = findStartEnd(img)

stack = search(start,end,pix,img)



print(stack)



























