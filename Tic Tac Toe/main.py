from TicTacToe import TicTacToe

def showMenu():
    print("Press 1, 2, 3 to select")
    print("\t1. Show Rule")
    print("\t2. Start New Game")
    print("\t3. Exit")

while(True):
    tictactoeGame = TicTacToe()
    showMenu()
    key = input()
    if key == "1":
        tictactoeGame.showRule()
    elif key == "2":
        tictactoeGame.startNewGame()
    elif key == "3":
        break
    else:
        print("Invalid input. Please select again!")
