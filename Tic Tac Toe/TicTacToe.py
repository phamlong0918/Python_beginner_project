class TicTacToe:
    def __init__(self) -> None:
        self.__grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def showRule(self) -> None:
        print("Rule: The object of Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing Xs and Os on the game board until either oppent has three in a row or all nine squares are filled. X always goes first, and in the event that no one has three in a row, the stalemate is called a cat game.")
        print("This is all positions: ")
        for i in range(1, 10):
            if i % 3 != 0:
                print(i, end="|")
            else:
                print(i)
        print("Please press any key to play!")
        key = input()


    def startNewGame(self):
        firstPlayer = 1
        secondPlayer = 2
        player = firstPlayer
        self.__showGrid()
        while(self.__getWinner() == -1):
            print("Player: ", player, ": ", end="")
            pos = int(input())
            if any([pos < 1, pos > 9]):
                print("Invalid position, please enter again")
                continue

            row: int = int((pos - 1) / 3)
            col: int = int((pos - 1) % 3)

            if self.__grid[row][col] != 0:
                print("his cell is not available, please enter again!")
                continue

            self.__grid[row][col] = player
            self.__showGrid()

            # change player
            if player == firstPlayer:
                player = secondPlayer
            else:
                player = firstPlayer

        winner: int = self.__getWinner()
        if winner == 0:
            print("--- Draw ---")
        else:
            print("--- Player ", winner, " win ---")

        key = input("Please press any key to exit!")

    def __showGrid(self):
        for i in range(3):
            for j in range(3):
                if self.__grid[i][j] == 1:
                    print("X", end="")
                elif self.__grid[i][j] == 2:
                    print("O", end="")
                else:
                    print("", end="")

                if j < 2:
                    print("\t|\t", end="")

            print("")

    def __getWinner(self):
        """
        return 1 if player 1 win
        return 2 if player 2 win
        return 0 if draw
        return -1 if the game has still not end
        """

        if any([all([self.__grid[0][0] == 1, self.__grid[0][1] == 1, self.__grid[0][2] == 1]),
                all([self.__grid[1][0] == 1, self.__grid[1][1] == 1, self.__grid[1][2] == 1]),
                all([self.__grid[2][0] == 1, self.__grid[2][1] == 1, self.__grid[2][2] == 1])]):
            return 1

        if any([all([self.__grid[0][0] == 1, self.__grid[1][0] == 1, self.__grid[2][0] == 1]),
                all([self.__grid[0][1] == 1, self.__grid[1][1] == 1, self.__grid[2][1] == 1]),
                all([self.__grid[0][2] == 1, self.__grid[1][2] == 1, self.__grid[2][2] == 1])]):
            return 1

        if any([all([self.__grid[0][0] == 1, self.__grid[1][1] == 1, self.__grid[2][2] == 1]),
                all([self.__grid[0][2] == 1, self.__grid[1][1] == 1, self.__grid[2][0] == 1])]):
            return 1
        
        if any([all([self.__grid[0][0] == 2, self.__grid[0][1] == 2, self.__grid[0][2] == 2]),
                all([self.__grid[1][0] == 2, self.__grid[1][1] == 2, self.__grid[1][2] == 2]),
                all([self.__grid[2][0] == 2, self.__grid[2][1] == 2, self.__grid[2][2] == 2])]):
            return 2

        if any([all([self.__grid[0][0] == 2, self.__grid[1][0] == 2, self.__grid[2][0] == 2]),
                all([self.__grid[0][1] == 2, self.__grid[1][1] == 2, self.__grid[2][1] == 2]),
                all([self.__grid[0][2] == 2, self.__grid[1][2] == 2, self.__grid[2][2] == 2])]):
            return 2

        if any([all([self.__grid[0][0] == 2, self.__grid[1][1] == 2, self.__grid[2][2] == 2]),
                all([self.__grid[0][2] == 2, self.__grid[1][1] == 2, self.__grid[2][0] == 2])]):
            return 2

        for i in range(3):
            for j in range(3):
                if self.__grid[i][j] == 0:
                    return -1

        return 0