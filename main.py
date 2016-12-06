from Board import *
import time

def main():
    printInstructions()

    while True:
        board = Board()
        difficulty = getDifficulty()
        playRound(board, difficulty)

        choice = raw_input("\nPlay again? y/n\n")
        if choice is not "y":
            print("Thanks for playing!")
            return


def playRound(board, difficulty):
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
        if board.isWon():
            print("\nYou Won!")
            return
        elif board.isDraw():
            print("\nDraw.")
            return

        #Computer chooses position, check for win
        board.setAI(difficulty)
        if board.isWon():
            board.showBoard()
            print("\nYou lost.")
            return
        elif board.isDraw():
            board.showBoard()
            print("\nDraw.")
            return

def printInstructions():
    '''Print gameplay instructions to user'''
    print("Tic-Tac-Toe")
    print("___________")
    print("Choose coordinates (row,column) when prompted.")
    print("     eg. 20 represents row 2, column 0.")
    print("Good Luck!\n\n")


def getDifficulty():
    print("\nChoose difficulty: ")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")

    return int(raw_input())


def choosePosition():
    '''get user input for coords'''
    coords = raw_input("Place 'X' at: ")
    row = int(coords[0])
    col = int(coords[1])
    return (row, col)

if __name__ == "__main__":
    main()
