from Board import *
import time

def main():
    board = Board()
    printInstructions()

    playing = True
    while playing:
        board.reset()
        playRound(board)

        choice = input("\nPlay again? y/n")
        if choice is not "y":
            print("Thanks for playing!")
            playing = False


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


        print("Computer's turn . . .")
        time.sleep(1)
        board.setRand()
        if board.isWon():
            showBoard()
            print("\nYou lost.")
            return


def choosePosition():
    '''get user input for coords'''
    coords = raw_input("Place 'X' at: ")
    row = int(coords[0])
    col = int(coords[1])
    return (row, col)

if __name__ == "__main__":
    main()
