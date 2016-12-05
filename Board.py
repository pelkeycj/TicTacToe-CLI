class Board():
    def __init__(self):
        self.grid = [[" " for x in range(3)] for y in range(3)]

    def grid(self):
        return self.grid

    def showBoard(self):
        '''Display board'''
        print(" A  B  C")
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
