visited = [1,2,3,4,5,6,7,8,9]

move = 10

if((254,0,0) >= (220,220,200)):
    print("Nem tartalmazza")
else:
    print("tartalmazza")


class Move:
    def __init__(self,coordinate,parent):
        self.coordinate = coordinate
        self.parent = parent


movesList = []

for i in range(1,10):
    j = i + 1
    if len(movesList) > 0:
        parrent = movesList[len(movesList)-1].coordinate
    else:
        parrent = (-1,-1)
    movesList.append(Move((i,j),parrent))


for move in movesList:
    print(str(move.parent))