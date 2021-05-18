import numpy as np
import random
from PIL import Image


def show(img):
    imgScaled = img.resize((600,600))
    imgScaled.show()

def findEnds(img):
    array = np.array(img)

    start = (254,0,0)
    end = (0,9,254)

    Ys, Xs = np.where(np.all(array == start,axis=2))
    Ye, Xe = np.where(np.all(array == end,axis=2))

    start_loc = (Xs[0],Ys[0])
    end_loc = (Xe[0],Ye[0])

    return start_loc, end_loc

def search(start,end,img,pix):
    isFound = False
    current = start
    array = np.array(img)
    path = []
    intersects = []

    while not isFound:
        possible = []
        surroundings = [(current[0]-1,current[1]),
                        (current[0]+1,current[1]),
                        (current[0],current[1]-1),
                        (current[0],current[1]+ 1)]
        for move in surroundings:
            if end == move:
                isFound = True
            if((pix[move] >= (200,200,200)) and pix[move] != (255,255,0) and move != start):
                possible.append(move)

        if len(possible) >= 2:
            if current not in intersects:
                intersects.append(current)

        if len(possible) == 0:
            intersects_reversed = intersects[::-1]
            for i in intersects_reversed:
                if  i != current:
                    current = i
                    intersects.pop(intersects.index(i))
                    break
            path = path[:path.index(current)]
        else:
            current = random.choice(possible)

        path.append(current)
        array[current[1],current[0]] = (255,255,0)
        img = Image.fromarray(array)
        pix = img.load()

    for p in path[:-1]:
        array[p[1],p[0]] = (0,255,0)
    img = Image.fromarray(array)
    img.save('solution.png')

#Labirintus megadás
img = Image.open("maze2.png")
pix = img.load()


start, end = findEnds(img)
search(start,end,img,pix)
print(str(start))
print(str(end))




