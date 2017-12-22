#Fix starting at random places when in corner
#Fix index error at corners
#Fix going back and forth between boxes(add a variable that has the previous move)
#See why assertions are causing issues
#Print what the thing is doing after it does it

from zellegraphics import *
from random import *
from time import sleep
import sys

#Box class
class Box(Rectangle):

    #Static Vars
    prevList=[]
    obstacles= []
    tiles=[]

    #Initialization
    def __init__(self, p1, p2, obstacle, col, row):
        Rectangle.__init__(self, p1, p2)

        self.obstacle= obstacle
        self.row= row
        self.col= col
        self.startTile= False

        if self.obstacle:
            self.setFill("black")
            self.obstacles.append(self)
        else:
            self.setFill("snow")

    #isObstacle
    def isObstacle(self):
        return self.obstacle

    #GetLocation
    def getLoc(self):
        return self.col, self.row

    #SetStart
    def setStart(self):
        self.startTile= True
        self.setFill("green")

    #isStart
    def isStart(self):
        return self.startTile

    #moveUp
    def moveUp(self):
        try:
            return grid[self.col][self.row-1], "u"
        except:
            IndexError

    #moveDown
    def moveDown(self):
        try:
            return grid[self.col][self.row+1], "d"
        except:
            IndexError

    #moveLeft
    def moveLeft(self):
        try:
            return grid[self.col-1][self.row], "l"
        except:
            IndexError

    #moveRight
    def moveRight(self):
        try:
            return grid[self.col+1][self.row], "r"
        except:
            IndexError

    #prevCheck
    def prevCheck(self, opp):

        dic= {"u": self.moveUp(), "d": self.moveDown() , "l": self.moveLeft() ,
          "r": self.moveRight(),
              self.moveUp(): "d", self.moveDown(): "u", self.moveRight(): "l",
              self.moveLeft(): "r"}

        length= len(self.prevList)

        if length>0:
            if self.prevList[length-1] != opp:
                futurebox, prev= dic[opp]
            else:
                futurebox, prev= dic[dic[dic[opp]]]
        else:
            futurebox, prev= dic[opp]

        return futurebox, prev

    #seekX
    def seekX(self, diffX, diffY, prev):

        #If the difference is positive, go right 
        if diffX>0:
            '''futurebox, prev= self.moveRight()'''

            futurebox, prev= self.prevCheck("r")

            if futurebox.isObstacle():
                print("X: Cannot move {} {}".format(prev, self))

                #Don't want to go left, so try up and down
                #If the difference is positive, go down first
                if diffY> 0:
                    futurebox, prev= self.prevCheck("d")

                    if futurebox.isObstacle():
                        print("X: Cannot move {} {}".format(prev, self))
                        futurebox, prev= self.prevCheck("u")

                        if futurebox.isObstacle():
                            print("X: Cannot move {} {}".format(prev, self))
                            futurebox, prev= self.prevCheck("l")

                            if futurebox.isObstacle():
                                print("X: cannot move {} {}".format(prev, self))
                                print("X: Trapped!")

                #If the difference is negative, go up first
                else:
                    assert diffY< 0, ("Value of diffY is %s" %diffY)
                    futurebox, prev= self.prevCheck("u")

                    if futurebox.isObstacle():
                        print("X: Cannot move {] {}".format(prev, self))
                        futurebox, prev= self.prevCheck("d")

                        if futurebox.isObstacle():
                            print("X: Cannot move {} {}".format(prev,self))
                            futurebox, prev= self.prevCheck("l")

                            if futurebox.isObstacle():
                                print("X: Cannot move {} {}".format(prev, self))
                                print("X: Trapped!")

        #If the difference is negative, go left                                       
        else:
            assert diffX< 0, ("Value of diffX is %s" %diffX)
            '''futurebox, prev= self.moveLeft()'''
            futurebox, prev= self.prevCheck("l")
            
            if futurebox.isObstacle():
                print("X: Cannot move left %s" %self)

                #Don't want to go right, so try up and down
                #If the difference is positive, go down first
                if diffY> 0:
                    futurebox, prev= self.moveDown()

                    if futurebox.isObstacle():
                        print("X: Cannot move down %s" %self)
                        futurebox, prev= self.moveUp()

                        if futurebox.isObstacle():
                            print("X: Cannot move up %s" %self)
                            futurebox, prev= self.moveRight()

                            if futurebox.isObstacle():
                                print("X: Cannot move right %s" %self)
                                print("X: Trapped!")
                                sys.exit()
                                
                #If the difference is negative, go up first
                else:
                    assert diffY< 0, ("Value of diffY is %s" %diffY)
                    futurebox, prev= self.moveUp()

                    if futurebox.isObstacle():
                        print("X: Cannot move up %s" %self)
                        futurebox, prev= self.moveDown()

                        if futurebox.isObstacle():
                            print("X: Cannot move down %s" %self)
                            futurebox, prev= self.moveRight()

                            if futurebox.isObstacle():
                                print("X: Cannot move right %s" %self)
                                print("X: Trapped!")
                                sys.exit()

        return futurebox, prev

    def seekY(self, diffX, diffY, prev):

        dic= {"u": self.moveUp(), "d": self.moveDown() , "l": self.moveLeft() ,
          "r": self.moveRight(), self.moveUp(): "u"}
        
        if diffY>0:
            futurebox, prev= self.moveDown()

            if futurebox.isObstacle():
                print("Y: Cannot move down %s" %self)

                if diffX> 0:
                    futurebox, prev= self.moveRight()

                    if futurebox.isObstacle():
                        print("Y: Cannot move right %s" %self)
                        futurebox, prev= self.moveLeft()

                        if futurebox.isObstacle():
                            print("Y: Cannot move left %s" %self)
                            futurebox, prev= self.moveUp()

                            if futurebox.isObstacle():
                                print("Y: Cannot move up %s" %self)
                                print("Y: Trapped!")
                                sys.exit()
                                

                else:
                    assert diffX< 0, ("Value of diffX is %s" %diffX)
                    futurebox, prev= self.moveLeft()

                    if futurebox.isObstacle():
                        print("Y: Cannot move left %s" %self)
                        futurebox, prev= self.moveRight()

                        if futurebox.isObstacle():
                            print("Y: Cannot move right %s" %self)
                            futurebox, prev= self.moveUp()

                            if futurebox.isObstacle():
                                print("Y: Cannot move up %s" %self)
                                print("Y: Trapped!")
                                sys.exit()
                                       
        else:
            assert diffY< 0, ("Value of diffY is %s" %diffY)
            futurebox, prev= self.moveUp()

            if futurebox.isObstacle():
                print("Y: Cannot move up %s" %self)
                
                if diffX> 0:
                    futurebox, prev= self.moveRight()

                    if futurebox.isObstacle():
                        print("Y: Cannot move right %s" %self)
                        futurebox, prev= self.moveLeft()

                        if futurebox.isObstacle():
                            print("Y: Cannot move left %s" %self)
                            futurebox, prev= self.moveDown()

                            if futurebox.isObstacle():
                                print("Y: Cannot move down %s" %self)
                                print("Y: Trapped!")
                                sys.exit()

                else:
                    assert diffX< 0, ("Value of diffX is ", diffX)
                    futurebox, prev= self.moveLeft()

                    if futurebox.isObstacle():
                        print("Y: Cannot move left %s" %self)
                        futurebox, prev= self.moveRight()

                        if futurebox.isObstacle():
                            print("Y: Cannot move right %s" %self)
                            futurebox, prev= self.moveDown()

                            if futurebox.isObstacle():
                                print("Y: Cannot move down %s" %self)
                                print("Y: Trapped!")
                                sys.exit()

        return futurebox, prev
    
    def pathFinderX(self, diffX, diffY, prev):

        box, prev= self.seekX(diffX, diffY, prev)

        self.tiles.append(box)
        
        if box != endingTile:           
            box.setFill("gold4")
        else:
            box.setFill("green")

        if self.isStart():   
           self.setFill("green")
        else:
            self.setFill("gold")

        sleep(2)

        self.prevList.append(prev)
        
        return box, prev               

    def pathFinderY(self, diffX, diffY, prev):

        box, prev= self.seekY(diffX, diffY, prev)

        self.tiles.append(box)
        
        if box != endingTile:           
            box.setFill("gold4")
        else:
            box.setFill("green")

        if self.isStart():   
           self.setFill("green")
        else:
            self.setFill("gold")

        sleep(2)

        self.prevList.append(prev)
        
        return box, prev

    def __str__(self):
        return "grid[{}, {}]".format(self.col, self.row)

#Window options
window= GraphWin("", 600, 600, autoflush=True)
window.setBackground("LightGoldenrod1")

#Creating the grid
print("Creating grid... \n")

x1, x2, row, col= 0, 50, 0, 0

grid= [ [0 for i in range(10) ] for i in range(10) ]

for col in range(10):
    x1+=50
    x2+=50
    y1, y2= 0, 50
    for row in range(10):
        obstacle= choice([False, False, False, True])
        y1+=50
        y2+=50
        grid[col][row]= Box(Point(x1, y1), Point(x2, y2), obstacle, col, row)

for col in grid:
    for row in col:
        row.draw(window)

#Starting tile
print("Choosing starting tile...")

currentTile= grid[randint(0, 9)][randint(0,9)]

while (currentTile.isObstacle()):
    print("Failure, %s" %currentTile)
    currentTile= grid[randint(0, 9)][randint(0,9)]

currentTile.setStart()
print("Success! %s \n" %currentTile)

#Ending tile
print("Choosing ending tile...")

endingTile= grid[randint(0, 9)][randint(0,9)]

while (endingTile.isObstacle() or endingTile == currentTile):
    print("Failure, %s" %endingTile)
    endingTile= grid[randint(0, 9)][randint(0,9)]

print("Success! %s \n" %endingTile)
endingTile.setFill("red")

endX, endY= endingTile.getLoc()
endX+=1
endY+=1

prev=""

#Loop
while currentTile != endingTile:

    currentX, currentY= currentTile.getLoc()
    currentX+=1
    currentY+=1

    diffY= endY-currentY
    diffX= endX-currentX

    if diffX != 0:
        currentTile, prev= currentTile.pathFinderX(diffX, diffY, prev)
    else:
        print("X was skipped")

    if diffY != 0:
        currentTile, prev= currentTile.pathFinderY(diffX, diffY, prev)
    else:
        print("Y was skipped")

print("")
print("Done!")
    

