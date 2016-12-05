import random

class Board():
    def __init__(self):
        self.grid = [[" " for x in range(3)] for y in range(3)]

    def reset(self):
        '''Resets to board to blank grid'''
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
