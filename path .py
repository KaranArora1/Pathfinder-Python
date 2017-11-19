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
    

