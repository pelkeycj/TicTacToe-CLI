from Board import *
import time

def main():
    printInstructions()

    while True:
        board = Board()
        playRound(board)

        choice = raw_input("\nPlay again? y/n\n")
        if choice is not "y":
            print("Thanks for playing!")
            return


def printInstructions():
    '''Print gameplay instructions to user'''
    print("Tic-Tac-Toe")
    print("___________")
    print("Choose coordinates (row,column) when prompted.")
    print("     eg. 20 , 00, etc.")
    print("Good Luck!\n\n")

def playRound(board):
    '''Play until win/lose'''
    while True:
        board.showBoard()
        row = 9
        col = 9

        #get user choice
        while not board.isValid(row, col):
            row, col = choosePosition()

        #set board and check for win
        board.setValue(row, col, "X")
        board.showBoard()
        if board.isWon():
            print("\nYou Won!")
            return
        elif board.isDraw():
            print("\nDraw.")
            return

        #Computer chooses position, check for win
        print("Computer's turn . . .")
        time.sleep(.5)
        board.setAI()
        if board.isWon():
            board.showBoard()
            print("\nYou lost.")
            return
        elif board.isDraw():
            board.showBoard()
            print("\nDraw.")
            return


def choosePosition():
    '''get user input for coords'''
    coords = raw_input("Place 'X' at: ")
    row = int(coords[0])
    col = int(coords[1])
    return (row, col)

if __name__ == "__main__":
    main()
