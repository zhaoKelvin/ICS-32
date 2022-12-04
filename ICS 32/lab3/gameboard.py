class BoardClass:
    """A class which contains the functionality of Tic Tac Toe.
    
    Attributes:
        p1_username (str): User name of player 1
        p2_username (str): User name of player 2
        last_player (str): User name of the last player to have a turn
        games_played (int): Number of games both players played together
        game_board (list[list[str]]): Current state of the board
        
        p1_wins (int): Number of wins of player 1
        p2_wins (int): Number of wins of player 2
        
        p1_ties (int): Number of ties of player 1
        p2_ties (int): Number of ties of player 2
        
        p1_losses (int): Number of losses of player 1
        p2_losses (int): Number of losses of player 2
        """
        
    def __init__(self, p1_username: str, p2_username: str) -> None:
        """Initialize the BoardClass object."""
        self.p1_username = p1_username
        self.p2_username = p2_username
        self.last_player = self.p1_username
        self.games_played = 0
        self.game_board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        
        self.p1_wins = 0
        self.p2_wins = 0
        
        self.p1_ties = 0
        self.p2_ties = 0
        
        self.p1_losses = 0
        self.p2_losses = 0
    
    def updateGamesPlayed(self) -> None:
        """Updates the amount of games the players have played together."""
        self.games_played += 1
        
    def updateGamesWon(self, p_number: int) -> None:
        """Updates the amount of games won by desired player"""
        if (p_number == 1):
            self.p1_wins += 1
        
        if (p_number == 2):
            self.p2_wins += 1
    
    def updateGamesLost(self, p_number: int) -> None:
        """Updates the amount of games lost by desired player"""
        if (p_number == 1):
            self.p1_losses += 1
        
        if (p_number == 2):
            self.p2_losses += 1
            
    def updateGamesTied(self, p_number: int) -> None:
        """Updates the amount of games tied by desired player"""
        if (p_number == 1):
            self.p1_ties += 1
        
        if (p_number == 2):
            self.p2_ties += 1
        
    def resetGameBoard(self) -> None:
        """Resets the entire game board."""
        self.game_board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    def updateGameBoard(self, p_number: int, p_move: tuple[int, int], current_board: str) -> str:
        """Takes as input the player's number and their move in the format of a coordinate(tuple).
            
        Reconstructs the gameboard each element at a time using given current_board string.
        Then, use the player's inputted coordinate to update gameboard with the player's move.
        
        Return:
            A string of the current board state.
        """
        # example board string -> " _ | _ | _ \n---------\n _ | _ | _ \n---------\n _ | _ | _ "
        temp_board = list(current_board)
        row_counter = 0
        column_counter = 0
        for i in range(0, len(temp_board)):
            if (row_counter == 3):
                row_counter = 0
                column_counter += 1
            if (temp_board[i] == "X" or temp_board[i] == "O" or temp_board[i] == "_"):
                self.game_board[int(column_counter)][row_counter] = temp_board[i]
                row_counter += 1
        
        # implements inputted move
        if (p_number == 1):
            marker = "X"
        else:
            marker = "O"
        
        self.game_board[p_move[0] - 1][p_move[1] - 1] = marker
        
        return (f" {self.game_board[0][0]} | {self.game_board[0][1]} | {self.game_board[0][2]} "
                f"\n---------\n {self.game_board[1][0]} | {self.game_board[1][1]} | {self.game_board[1][2]} " 
                f"\n---------\n {self.game_board[2][0]} | {self.game_board[2][1]} | {self.game_board[2][2]} ")     
        

    def isWinner(self) -> int:
        """Checks each possible winning combination and updates wins and losses.
        
        Return:
            0 if there are no winners
            1 if player 1 is the winner
            2 if player 2 is the winner    
        """
        # Check rows
        for i in range(3):    
            if (self.game_board[i].count("X") == 3 or self.game_board[i].count("O") == 3):
                if (self.game_board[i][0] == "X"):
                    return 1
                else:
                    return 2

        # Check columns 
        for i in range(3):
            if (self.game_board[0][i] == "X" and self.game_board[1][i] == "X" and self.game_board[2][i] == "X"):
                return 1
            elif (self.game_board[0][i] == "O" and self.game_board[1][i] == "O" and self.game_board[2][i] == "O"):
                return 2
        
        # Check top-left to bottom-right diagonal for player 1
        for i in range(3):
            if (self.game_board[i][i] == "X"):
                if (i == 2):
                    return 1
            else:
                break
            
        # Check top-left to bottom-right diagonal for player 2
        for i in range(3):
            if (self.game_board[i][i] == "O"):
                if (i == 2):
                    return 2
            else:
                break
        
        # Check top-right to bottom-left diagonal for player 1
        for i, j in enumerate(range(2, -1, -1)):
            if (self.game_board[i][j] == "X"):
                if (j == 0):
                    return 1
            else:
                break
        
        # Check top-right to bottom-left diagonal for player 2
        for i, j in enumerate(range(2, -1, -1)):
            if (self.game_board[i][j] == "O"):
                if (j == 0):
                    return 2
            else:
                break
        
        # If no winning conditions are met, return 0
        return 0
            
    def updateLastMove(self, last_player: int) -> None:
        """Updates who moved last in the game. (Player 1 always goes last in event of a tie."""
        if (last_player == 1):
            self.last_player = self.p1_username
        else:
            self.last_player = self.p2_username

    def boardIsFull(self) -> int:
        """Iterates through game board, checks if there any open slots, and updates tie counter.
        
        Return:
            0 if board is not full
            1 if board is full
        """
        for row in self.game_board:
            for slot in row:
                if (slot == "_"):
                    return 0
        
        return 1

    def printStats(self, p_number: int) -> None:
        """Prints the player's statistics."""
        if (p_number == 1):
            print("Username:", self.p1_username)
            print("Last Move:", self.last_player)
            print("Number of games played:", self.games_played)
            print("Number of wins:", self.p1_wins)
            print("Number of losses:", self.p1_losses)
            print("Number of ties:", self.p1_ties)
        elif (p_number == 2):
            print("Username:", self.p2_username)
            print("Last Move:", self.last_player)
            print("Number of games played:", self.games_played)
            print("Number of wins:", self.p2_wins)
            print("Number of losses:", self.p2_losses)
            print("Number of ties:", self.p2_ties)
        else:
            print("Invalid Player")
            
    def printBoard(self, sent_board: str=0) -> None:
        """Prints current game board. If board argument is used, print sent board."""
        
        if (sent_board):
            print(sent_board)
        
        if (not sent_board):
            print(f" {self.game_board[0][0]} | {self.game_board[0][1]} | {self.game_board[0][2]} "
                    f"\n---------\n {self.game_board[1][0]} | {self.game_board[1][1]} | {self.game_board[1][2]} " 
                    f"\n---------\n {self.game_board[2][0]} | {self.game_board[2][1]} | {self.game_board[2][2]} ")
            
    def getBoard(self) -> None:
        """Returns a string of the board"""
        return (f" {self.game_board[0][0]} | {self.game_board[0][1]} | {self.game_board[0][2]} "
                f"\n---------\n {self.game_board[1][0]} | {self.game_board[1][1]} | {self.game_board[1][2]} " 
                f"\n---------\n {self.game_board[2][0]} | {self.game_board[2][1]} | {self.game_board[2][2]} ")
        
    def checkValidMove(self, p_move: tuple[int, int]) -> bool:
        """Returns true if move is valid, otherwise false."""
        x_index, y_index = p_move
        if (self.game_board[x_index - 1][y_index - 1] == "_"):
            return True
        else:
            return False