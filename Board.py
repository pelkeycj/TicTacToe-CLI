import random

class Board():
    def __init__(self):
        self.grid = [[" " for x in range(3)] for y in range(3)]

    def showBoard(self):
        '''Display board'''
        print(" 0  1  2")
        for row in range(3):
            line = str(row) + " "
            for col in range(3):
                if col == 2:
                    line += self.grid[row][col]
                else:
                    line += (self.grid[row][col] + "|")

            print(line)
            if row is not 2:
                print("  - - -")


    def isValid(self, row, col):
        '''Returns True if coordinates are valid
            and available'''
        if row > 2 or col > 2:
            return False
        elif self.grid[row][col] is not " ":
            return False
        else:
            return True

    def setValue(self, row, col, symbol):
        '''Sets symbol if valid coordinates'''
        self.grid[row][col] = symbol


    def setAI(self):
        '''Sets the AI position:
            win, block win, or random'''
        # try to win
        if self.setThird("O", "O"):
            return
        # try to block a win
        elif self.setThird("X", "O"):
            return
        #occupy center
        elif self.isValid(1, 1):
            self.setValue(1, 1, "O")
        # place random
        else:
            self.setRand()
            return


    def setThird(self, toFind, toInsert):
        '''Attempts to insert toInsert at position to fill a row/col/diag
            where toFind occupies two positions.
            True if successful'''
        for i in range(3):
            #variables to search adjacent
            x = (i + 1) % 3
            y = (i + 2) % 3

            #top-left -> bottom-right diagonal
            if self.grid[i][i] is " " and self.grid[x][x] is self.grid[y][y] is toFind:
                self.setValue(i, i, toInsert)
                return True
            #bottom-left -> top-right diagonal
            elif self.grid[i][2 - i] is " " and self.grid[x][2 - x] is self.grid[y][2 - y] is toFind:
                self.setValue(i, 2 - i, toInsert)
                return True

            for j in range(3):
                #horizontal
                if self.grid[j][i] is " " and self.grid[j][x] is self.grid[j][y] is toFind:
                    self.setValue(j, i, toInsert)
                    return True
                #vertical
                elif self.grid[i][j] is " " and self.grid[x][j] is self.grid[y][j] is toFind:
                    self.setValue(i, j, toInsert)
                    return True

        return False





    def setRand(self):
        '''Places 'O' at random available location'''
        random.seed()

        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)

            if self.isValid(row,col):
                self.setValue(row, col, "O")
                return

    def isWon(self):
        '''Determines whether game has been won'''
        #check horizontal
        for row in self.grid:
            if row[0] is row[1] is row[2] and row[0] is not" ":
                return True
        #check vertical
        for col in range(3):
            if self.grid[0][col] is \
              self.grid[1][col] is \
              self.grid[2][col] and\
              self.grid[0][col] is not " ":
               return True

        #check top-left -> bottom-right diagonal
        if self.grid[0][0] is self.grid[1][1] is self.grid[2][2] \
            and self.grid[0][0] is not " ":
            return True
        #check bottom-left -> top-right diagonal
        if self.grid[2][0] is self.grid[1][1] is self.grid[0][2] \
            and self.grid[2][0] is not " ":
            return True


    def isDraw(self):
        '''Determine whether the game ends in a draw'''
        for row in self.grid:
            for col in row:
                if col == " ":
                    return False
        return True
