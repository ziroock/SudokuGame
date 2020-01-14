#!/usr/bin/env python3
import random
from time import sleep
import turtle


class GameBoard:
    def __init__(self):
        self.grid = [[0 for x in range(9)] for y in range(9)]


    def clearBoard(self):
        self.grid = [[0 for x in range(9)] for y in range(9)]


    def printBoard(self):
        for row in self.grid:
            print(row)

    
    def copyBoard(self, grid_in):
        for row in range(9):
            for col in range(9):
                self.grid[row][col] = grid_in[row][col]


    def addNumber(self, number, row, col):
        if self.grid[row][col] < 0:
            print("Can't change this number!")
        elif self.grid[row][col] == 0:
            pritn("Number added successfuly!")


    def checkBoxesForDuplicates(self):
        boxes = [[0,0], [0,3], [0,6],
                [3,0], [3,3], [3,6],
                [6,0], [6,3], [6,6]]
        #helper function to check for a duplicate inside a spesific box
        def boxHasDuplicate(self, start):
            end_row = start[0] + 3
            end_col = start[1] + 3
            nums = [0]*9
            for row in range(start[0], end_row):
                for col in range(start[1], end_col):
                    #allows me to call a function, check puzzel so far
                    if self.grid[row][col] != 0:
                        if nums[self.grid[row][col] - 1] == 1:
                            return True
                        nums[self.grid[row][col] - 1] = 1
            return False

        #check each box!
        for pair in boxes:
            if boxHasDuplicate(self, pair):
                return False
        return True


    def checkColsForDuplicates(self):
        #helper function to check for duplicates inside a colomn
        def colHasDuplicate(self, col):
            nums = [0]*9
            for row in range(9):
                #allows me to call a function, check puzzel so far
                if self.grid[row][col] != 0:
                    if nums[self.grid[row][col] - 1] == 1:
                        return True
                    nums[self.grid[row][col] - 1] = 1
            return False

        #check all columns for duplicates
        for col in range(9):
            if colHasDuplicate(self, col):
                return False
        return True


    def checkRowsForDuplicates(self):

        def rowHasDuplicates(self, row):
            nums = [0]*9
            for item in self.grid[row]:
                if item != 0:
                    if nums[item - 1] == 1:
                        return True
                    nums[item - 1] = 1
            return False

        for row in range(9):
            # allows me to call a function, check puzzel so far
            if rowHasDuplicates(self, row):
                return False
        return True


    def checkSolution(self):
        return  self.checkRowsForDuplicates() and self.checkColsForDuplicates() and self.checkBoxesForDuplicates()


    def valDuplicatesInBox(self, val, row, col):
        start = []
        boxes = [[0,0], [0,3], [0,6],
            [3,0], [3,3], [3,6],
            [6,0], [6,3], [6,6]]
        for i in range(9):
            if row >= boxes[i][0] and col >= boxes[i][1] and row < boxes[i][0] + 3 and col < boxes[i][1] + 3:
                start = boxes[i]
        end_row = start[0] + 3
        end_col = start[1] + 3
        nums = [0]*9
        for row in range(start[0], end_row):
            for col in range(start[1], end_col):
                if self.grid[row][col] == val:
                    return True
        return False


    def valDuplicatesInCol(self, val, col):
        for row in self.grid:
            if row[col] == val:
                return True
        return False


    def checkIfBoardFull(self):
        for row in self.grid:
            for item in row:
                if item == 0:
                    return False
        return True


    #writes over current bard to populate a full board with random numbers
    def generateFullBoard(self):
        #clear Board so you start from scratch
        self.clearBoard()
        #Backtrack Function to get correct combination of numbers
        def fillBoard(self):
            possibleVals = [1,2,3,4,5,6,7,8,9]
            #there are 81 positions in the matrix to be populated
            for i in range(0 ,81):
                row = i // 9
                col = i % 9
                #if empty position try to find a fitting value
                if self.grid[row][col] == 0:
                    random.shuffle(possibleVals)
                    for val in possibleVals:
                        #if the value fitts the positon requirements aka single digit in its 
                        # row, in its col, and in its box
                        if val not in self.grid[row] and not self.valDuplicatesInCol(val, col) and not self.valDuplicatesInBox(val, row, col):
                            self.grid[row][col] = val
                            #if the grid is full, we are done
                            if self.checkIfBoardFull():
                                return True
                            # go to another random position
                            elif fillBoard(self):
                                return True
                    break
            #if non of the values fit at a position aka the value is False
            self.grid[row][col] = 0
            return False
        fillBoard(self)


###     TEMPORARY SOLUTION FOR VISUALIZATION (Will use a different tool to create a better design)
##############################################################################
#code snipped from "https://www.101computing.net/sudoku-generator-algorithm/""
##############################################################################
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")
myPen.hideturtle()
topLeft_x=-150
topLeft_y=150

def text(message,x,y,size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x,y)           
    myPen.write(message,align="left",font=FONT)

#A procedure to draw the grid on screen using Python Turtle
def drawGrid(grid):
    intDim=35
    for row in range(0,10):
        if (row%3)==0:
          myPen.pensize(3)
        else:
          myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x,topLeft_y-row*intDim)
        myPen.pendown()
        myPen.goto(topLeft_x+9*intDim,topLeft_y-row*intDim)
    for col in range(0,10):
        if (col%3)==0:
          myPen.pensize(3)
        else:
          myPen.pensize(1)    
        myPen.penup()
        myPen.goto(topLeft_x+col*intDim,topLeft_y)
        myPen.pendown()
        myPen.goto(topLeft_x+col*intDim,topLeft_y-9*intDim)

    for row in range (0,9):
      for col in range (0,9):
        if grid[row][col]!=0:
          text(grid[row][col],topLeft_x+col*intDim+9,topLeft_y-row*intDim-intDim+8,18)
##############################################################################
##########################      END CODE SNIPPED
##############################################################################


def main():
    # Test the graphics visiulization
    sudoku2 = GameBoard()
    sudoku2.generateFullBoard()
    drawGrid(sudoku2.grid)
    myPen.getscreen().update()
    sleep(15)


    #### TEST sudoku copyBoeard(grid) function ###########
    # grid = [[3,1,6,5,7,8,4,9,2],
    #         [5,2,9,1,3,4,7,6,8],
    #         [4,8,7,6,2,9,5,3,1],
    #         [2,6,3,4,1,5,9,8,7],
    #         [9,7,4,8,6,3,1,2,5],
    #         [8,5,1,7,9,2,6,4,3],
    #         [1,3,8,9,4,7,2,5,6],
    #         [6,9,2,3,5,1,8,7,4],
    #         [7,4,5,2,8,6,3,1,9]]
    # sudoku = GameBoard()
    # sudoku.copyBoard(grid)
    ############### END TEST ####################


    ########## TEST THE FULL BOARD GENERATOR TIME EFFICENCY ###########
    # start_time = time.time()
    # N = 1000
    # for i in range(N): 
    #     #print("Test #" + str(i))
    #     #sudoku2.printBoard()
    #     if not answer:
    #         print("You Fucked Up!")
    #         break
    #     sudoku2.generateFullBoard()
    #     answer = sudoku2.checkSolution()
    # print("Print time:")
    # print("--- %s seconds ---" % (time.time() - start_time) + " " + str(N)+ "# Tests Ran!")
    ################ END TEST #############################
    print("The game is in develepment stage!")
    return 0
main()