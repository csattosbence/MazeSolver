from PIL import Image
from typing import List

visited = [1,2,3,4,5,6,7,8,9]

move = 10



class Move:
    def __init__(self,coordinate,parent):
        self.coordinate = coordinate
        self.parent = parent



def contains(move:Move, moveList: List[Move]):
    for i in moveList:
        if(i.coordinate == move.coordinate):
            return True
        else:
            return False


movesList = []

for i in range(1,10):
    j = i + 1
    if len(movesList) > 0:
        parrent = movesList[len(movesList)-1].coordinate
    else:
        parrent = (-1,-1)
    movesList.append(Move((i,j),parrent))


testMove = Move((3,2),(2,-1))


for x in movesList[len(movesList)-2::-1]:
    print(x.coordinate)


img = Image.open("maze2.png")
pix = img.load()




