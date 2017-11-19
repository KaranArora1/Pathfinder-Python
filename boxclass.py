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
            obstacles.append(self)
        else:
            self.setFill("snow")
            tiles.append(self)

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
        return grid[self.col][self.row-1], "u"

    #moveDown
    def moveDown(self):
        return grid[self.col][self.row+1], "d"

    #moveLeft
    def moveLeft(self):
        return grid[self.col-1][self.row], "l"

    #moveRight
    def moveRight(self):
        return grid[self.col+1][self.row], "r"

    #seekX
    def seekX(self, diffX, diffY, prev):

        #If the difference is positive, go right 
        if diffX>0:
            futurebox, prev= self.moveRight()

            if futurebox.isObstacle():
                print("X: Cannot move right %s" %self)

                #Don't want to go left, so try up and down
                #If the difference is positive, go down first
                if diffY> 0:
                    futurebox, prev= self.moveDown()

                    if futurebox.isObstacle():
                        print("X: Cannot move down %s" %self)
                        futurebox, prev= self.moveUp()

                        if futurebox.isObstacle():
                            print("X: Cannot move up %s" %self)
                            futurebox, prev= self.moveLeft()

                            if futurebox.isObstacle():
                                print("X: cannot move left %s" %self)
                                print("X: Trapped!")

                #If the difference is negative, go up first
                else:
                    assert diffY< 0, ("Value of diffY is %s" %diffY)
                    futurebox, prev= self.moveUp()

                    if futurebox.isObstacle():
                        print("Cannot move up %s" %self)
                        futurebox, prev= self.moveDown()

                        if futurebox.isObstacle():
                            print("Cannot move down %s" %self)
                            futurebox, prev= self.moveLeft()

                            if futurebox.isObstacle():
                                print("X: Cannot move left")
                                print("X: Trapped!")

        #If the difference is negative, go left                                       
        else:
            assert diffX< 0, ("Value of diffX is %s" %diffX)
            futurebox, prev= self.moveLeft()
            
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

        tiles.append(box)
        
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

        print(self.prevList)
        
        return box, prev               

    def pathFinderY(self, diffX, diffY, prev):

        box, prev= self.seekY(diffX, diffY, prev)

        tiles.append(box)
        
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
        
        print(self.prevList)
        
        return box, prev

    def __str__(self):
        return "grid[{}, {}]".format(self.col, self.row)