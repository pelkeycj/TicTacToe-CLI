from Board import *
import random
import time

def main():
    board = Board()
    printInstructions()

    playing = True
    while playing:
        board.reset()
        playRound()

        choice = input("\nPlay again? y/n")
        if choice is not "y":
            print("Thanks for playing!")
            playing = False


def printInstructions():
    print("Tic-Tac-Toe")
    print("___________")
    print("Choose coordinates (row,column) when prompted.")
    print("     eg. 20 , 00, etc.")
    print("Good Luck!")

def choosePosition():
    coords = input("Place 'X' at: ")
    row = int(coords[0])
    col = int(coords[1])
    return (row, col)

def playRound(board):
    while True:
        board.showBoard()
        row, col = -1

        #get user choice
        while !board.isValid(row, col):
            row,col = choosePosition()

        #set board and check for win
        board.setValue(row, col, "X")
        board.showBoard()
        if board.isWon():
            print("\nYou Won!")
            return


        print("Computer's turn . . .")
        time.sleep(2)
        board.setRand()
        board.showBoard()
        if board.isWon():
            print("\nYou lost.")

if __name__ == "__main__":
    main()
