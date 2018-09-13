
##basematrix = [["#", "#", "#", "#", "#"],
##              ["#", "#", "#", "#", "#"],
##              ["#", "#", "#", "#", "#"],
##              ["#", "#", "#", "#", "#"],
##              ["#", "#", "#", "#", "#"]]

##movements = {"up" : "up",
##            "u" : "up",
##            "north" : "up",
##            "n" : "up",
##            "right" : "right",
##            "r" : "right",
##            "east" : "right",
##            "e" : "right",
##            "down" : "down",
##            "d" : "down",
##            "south" : "down",
##            "s" : "down",
##            "left" : "left",
##            "l" : "left",
##            "west" : "left",
##            "w" : "left"}

import random
import msvcrt

def SnakeGame(x_max_input=15, y_max_input=8, startLength = 4, tailGrowth = 4):
    movements = {b'w' : "up",
                b'd' : "right",
                b's' : "down",
                b'a' : "left"}

    def move(x):
        return movements.get(x.lower(), "")

    MAX_X = x_max_input
    MAX_Y = y_max_input

    TAIL_GROWTH = 5

    userIn = ""
    headPos = (MAX_X//2,MAX_Y//2)
    tailList = []
    tailMax = startLength

    def makeBiscuit():
        newBisc = headPos
        while ((newBisc == headPos) or (newBisc in tailList)):
            newBisc = (random.randrange(1, MAX_X+1), random.randrange(1, MAX_Y+1))
        return newBisc

    biscuitPos = makeBiscuit()

    gameOver = 0
    while userIn.lower() != "exit" and gameOver == 0:
        if(move(userIn)=="up" and headPos[1]>1):
            tailList.append(headPos)
            headPos = (headPos[0], headPos[1]-1)
        elif(move(userIn)=="right" and headPos[0]<MAX_X):
            tailList.append(headPos)
            headPos = (headPos[0]+1, headPos[1])
        elif(move(userIn)=="down" and headPos[1]<MAX_Y):
            tailList.append(headPos)
            headPos = (headPos[0], headPos[1]+1)
        elif(move(userIn)=="left" and headPos[0]>1):
            tailList.append(headPos)
            headPos = (headPos[0]-1, headPos[1])

        if (len(tailList)>=MAX_X*MAX_Y-1 and not headPos in tailList):
            gameOver = 2
        else:
            if len(tailList)>tailMax:
                tailList.pop(0)
            if headPos in tailList:
                gameOver = 1        
            if (headPos == biscuitPos):
                tailMax += TAIL_GROWTH
                biscuitPos = makeBiscuit()

        mapstring = ""
        for i in range(1,MAX_Y+1):
            for j in range(1,MAX_X+1):
                if ((j, i) == headPos and (j,i) in tailList):
                    mapstring += "X "
                elif((j, i) == headPos):
                    mapstring += "O "
                elif((j,i) in tailList):
                    mapstring += "x "
                elif((j,i) == biscuitPos):
                    mapstring += "M "
                else:
                    mapstring += "# "
            mapstring += "\n\n"
        print("\n"*50+mapstring)
        
        if gameOver == 0:
            userIn = msvcrt.getch()
        elif gameOver == 1:
            print("\nGame over!")
        else:
            print("\nYou win!")
    
