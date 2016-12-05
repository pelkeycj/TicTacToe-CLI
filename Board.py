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
            elif grid[row][col] is not " ":
                return False
            else:
                return True

    def setValue(self, row, col, symbol):
        '''Sets symbol if valid coordinates'''
            self.grid[row][col] = symbol

    def setRand(self):
        random.seed()

        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)

            if isValid(row,col):
                setValue(row, col, "O")
                return
                
