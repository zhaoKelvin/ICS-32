from gameboard import BoardClass
import socket
import tkinter as tk

class Player2:
    """Player 2 interactive GUI which hosts the server for Player 1."""
    
    def __init__(self) -> None:
        """Initialize the Tic Tac Toe game and related GUI components."""
        self.game = BoardClass()
        self.game.p1_username = ""
        self.game.p2_username = ""
        self.game.last_player = ""
        
        # Set up the GUI
        self.root = tk.Tk()
        self.root.title("Player Two")
        self.root.geometry("600x600")
        self.root.configure(background="lightgreen", border="10", borderwidth="10")
        self.root.resizable(0, 0)
        
        self.main_window = tk.Frame(self.root)
        self.main_window.pack(fill="both")
        
        # Create tk variables
        self.host_info = tk.StringVar()
        #self.host_info.set("127.0.0.1")
        self.port_info = tk.IntVar()
        #self.port_info.set(65432)
        self.p1_username = tk.StringVar()
        self.p2_username = tk.StringVar()
        self.last_player = tk.StringVar()
        self.game_stats = tk.StringVar()
        self.opponent_move = tk.StringVar()
        self.current_turn = tk.StringVar()
        
        self.buttons: list[tk.StringVar] = []
        for i in range(9):
            self.btn = tk.StringVar()
            self.buttons.append(self.btn)

        # Create GUI Appearance
        # Host/Port Input
        self.start_widget = tk.Frame(self.main_window)
        self.start_widget.pack()
        
        self.host_label = tk.Label(self.start_widget, text="HOST", font=("American Typewriter", 24))
        self.host_label.grid(row=0, column=0)
        
        self.host_entry = tk.Entry(self.start_widget, background="grey", textvariable=self.host_info, font=("American Typewriter", 24))
        self.host_entry.grid(row=0, column=1)
        
        self.port_label = tk.Label(self.start_widget, text="PORT", font=("American Typewriter", 24))
        self.port_label.grid(row=1, column=0)
        
        self.port_entry = tk.Entry(self.start_widget, background="grey", textvariable=self.port_info, font=("American Typewriter", 24))
        self.port_entry.grid(row=1, column=1)
        
        self.connect_button = tk.Button(self.start_widget, text="Send", command=self.connectToServer)
        self.connect_button.grid(row=1, column=2)
        
        # Send Username Input
        self.username_label = tk.Label(self.start_widget, text="Send Username", font=("American Typewriter", 24))
        self.username_label.grid(row=3, column=0)
        
        self.username_entry = tk.Entry(self.start_widget, background="grey", textvariable=self.p2_username, font=("American Typewriter", 24))
        self.username_entry.grid(row=3, column=1)
        
        self.send_button = tk.Button(self.start_widget, text="Send", 
                                     command= lambda: self.sendAndReceiveUsername(2, self.p2_username.get()))
        self.send_button.grid(row=3, column=2)
        
        self.spacer2 = tk.Label(self.start_widget)
        self.spacer2.grid(row=4, columnspan=2)
        
        # Game Stats
        self.stats = tk.Frame(self.main_window)
        self.stats.pack()
        
        self.current_turn.set(self.game.p1_username)
        self.current_player_label = tk.Label(self.stats, background="grey", width=15, textvariable=self.current_turn, 
                                          font=("American Typewriter", 24))
        self.current_player_label.grid(row=0, column=0)
        
        self.game_stats.set(self.game.getStats(2))
        self.game_stats_label = tk.Label(self.stats, width=40, height=5, textvariable=self.game_stats)
        self.game_stats_label.grid(row=0, column=1)
        
        # Game Board GUI
        self.board = tk.Frame(self.main_window, pady=30)
        self.board.pack()
        
        self.tiles = []
        for i in range(9):
            self.tile = tk.Button(self.board, height=3, width=5, bd=0.5, textvariable=self.buttons[i], font=("", 24),
                                command= lambda c=i: self.sendAndReceiveMove(f"{c//3+1}, {c%3+1}", c)).grid(row=i//3, column=i%3)
            self.tiles.append(self.tile)
        
        
        
        # When each game is over send message asking player 1 if want to play again, if not, then send another message of player stats

        self.root.mainloop()
        self.initial_server.close()
        
    def connectToServer(self) -> None:
        """Creates a server and binds connection to server."""
        self.initial_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.initial_server.bind((self.host_info.get(), self.port_info.get()))
        self.initial_server.listen()
        
        self.connection, self.address = self.initial_server.accept()
            
    def closeConnection(self) -> None:
        """Closes connection to a server."""
        self.connection.close()
        
    def sendAndReceiveUsername(self, player_num: int, username: str) -> None:
        """Sends and receives the username of connected server player 1 and receives first move of player 1."""
        # send username to opponent
        self.connection.sendall(username.encode())
        
        # for player 1
        if (player_num == 1):
            self.p1_username.set(username)
            opponent_username = self.connection.recv(1024).decode()
            self.p2_username.set(opponent_username)
            self.game.setUsername(1, username)
            self.game.setUsername(2, opponent_username)
        # for player 2
        if (player_num == 2):
            self.p2_username.set(username)
            opponent_username = self.connection.recv(1024).decode()
            self.p1_username.set(opponent_username)
            self.game.setUsername(2, username)
            self.game.setUsername(1, opponent_username)
            
            # set current player
            self.current_turn.set(self.game.p1_username)
            self.root.update()
            
            # receive opponent's move first move
            opponent_move = self.connection.recv(1024).decode()
            
            # implement opponent move into own board
            converted_move = self.convertMove(opponent_move[:-1])
            self.game.updateGameBoard(1, converted_move, self.game.getBoard())
            
            self.buttons[int(opponent_move[-1])].set("X")
            self.last_player.set(self.p1_username.get())
            self.game.updateLastMove(1)
            self.current_turn.set(self.game.p2_username)
            self.root.update()
        
    def sendAndReceiveMove(self, position: str, c: int) -> None:
        """Sends and receives moves through socket connection. 
        
        Checks for winnings and tie cases after implementing move into own board. If a game-ending case occurs, 
        waits for player 1's decision to continue or stop playing.
        """
        # send move to opponent
        self.connection.sendall((position + str(c)).encode())
        
        # implement own move into own board
        converted_move = self.convertMove(position)
        print(self.game.updateGameBoard(2, converted_move, self.game.getBoard()))
        
        self.buttons[c].set("O")
        self.last_player.set(self.p2_username.get())
        self.game.updateLastMove(2)
        self.current_turn.set(self.game.p1_username)
        self.root.update()
        
        # check if own move ties or wins you the game
        if (self.game.isWinner()):
            self.game.updateGamesPlayed()
            self.game.updateGamesWon(2)
            play_again = self.connection.recv(1024).decode()
            if (play_again == "Play Again"):
                self.resetGuiBoard()
                self.root.update()
                # receive opponent's move
                opponent_move = self.connection.recv(1024).decode()
                
                # implement opponent move into own board
                converted_move = self.convertMove(opponent_move[:-1])
                self.game.updateGameBoard(1, converted_move, self.game.getBoard())
                
                self.buttons[int(opponent_move[-1])].set("X")
                self.last_player.set(self.p1_username.get())
                self.game.updateLastMove(1)
                self.current_turn.set(self.game.p2_username)
                self.root.update()
            else:
                self.endMessageWindow("Fun Times")
            return None
        
        if (self.game.boardIsFull()):
            self.game.updateGamesPlayed()
            self.game.updateGamesTied(2)
            play_again = self.connection.recv(1024).decode()
            if (play_again == "Play Again"):
                self.resetGuiBoard()
                self.root.update()
                # receive opponent's move
                opponent_move = self.connection.recv(1024).decode()
                
                # implement opponent move into own board
                converted_move = self.convertMove(opponent_move[:-1])
                self.game.updateGameBoard(1, converted_move, self.game.getBoard())
                
                self.buttons[int(opponent_move[-1])].set("X")
                self.last_player.set(self.p1_username.get())
                self.game.updateLastMove(1)
                self.current_turn.set(self.game.p2_username)
                self.root.update()
            else:
                self.endMessageWindow("Fun Times")
            return None
            
        # receive opponent's move
        opponent_move = self.connection.recv(1024).decode()
        
        # implement opponent move into own board
        converted_move = self.convertMove(opponent_move[:-1])
        self.game.updateGameBoard(1, converted_move, self.game.getBoard())
        
        self.buttons[int(opponent_move[-1])].set("X")
        self.last_player.set(self.p1_username.get())
        self.game.updateLastMove(1)
        self.current_turn.set(self.game.p2_username)
        self.root.update()
        
        
        # check if opponent move ties or wins the game
        if (self.game.isWinner()):
            self.game.updateGamesPlayed()
            self.game.updateGamesLost(2)
            play_again = self.connection.recv(1024).decode()
            if (play_again == "Play Again"):
                self.resetGuiBoard()
                self.root.update()
                # receive opponent's move
                opponent_move = self.connection.recv(1024).decode()
                
                # implement opponent move into own board
                converted_move = self.convertMove(opponent_move[:-1])
                self.game.updateGameBoard(1, converted_move, self.game.getBoard())
                
                self.buttons[int(opponent_move[-1])].set("X")
                self.last_player.set(self.p1_username.get())
                self.game.updateLastMove(1)
                self.current_turn.set(self.game.p2_username)
                self.root.update()
            else:
                self.endMessageWindow("Fun Times")
            return None
        
        if (self.game.boardIsFull()):
            self.game.updateGamesPlayed()
            self.game.updateGamesTied(2)
            play_again = self.connection.recv(1024).decode()
            if (play_again == "Play Again"):
                self.resetGuiBoard()
                self.root.update()
                # receive opponent's move
                opponent_move = self.connection.recv(1024).decode()
                
                # implement opponent move into own board
                converted_move = self.convertMove(opponent_move[:-1])
                self.game.updateGameBoard(1, converted_move, self.game.getBoard())
                
                self.buttons[int(opponent_move[-1])].set("X")
                self.last_player.set(self.p1_username.get())
                self.game.updateLastMove(1)
                self.current_turn.set(self.game.p2_username)
                self.root.update()
            else:
                self.endMessageWindow("Fun Times")
            return None
        
        
    def convertMove(self, string_position: str) -> tuple[int, int]:
        """Convert inputted move from a string into a tuple of ints."""
        temp = string_position.split(", ")
        for i in range(2):
            e = int(temp.pop(0))
            temp.append(e)
        
        return tuple(temp)
    
    def endMessageWindow(self, message: str) -> None:
        """Creates an message, which contains final statistics that is displayed to the user
        
        Also contains a button which allows the player to or quit the GUI and session. 
        """
        self.endMsg = tk.Toplevel()
        self.endMsg.title("The Game Ended")
        tk.Label(self.endMsg, text=message).grid(row=0, columnspan=2)
        
        # get the final stats
        self.game_stats.set(self.game.getStats(2))
        self.game_stats_label = tk.Label(self.endMsg, textvariable=self.game_stats)
        self.game_stats_label.grid(row=1, columnspan=2)
        
        tk.Button(self.endMsg, text="Quit Game", command=self.quitGame).grid(row=2, column=1)
        
    def sendMessageToOpponent(self, message: str) -> None:
        """Send a simple message through the socket connection."""
        self.connection.sendall(message.encode())
    
    def resetGuiBoard(self) -> None:
        """Reset both the tkinter GUI board, the model gameboard board, and notifies opponent to continue playing."""
        for i in range(9):
            self.buttons[i].set("")
        self.game.resetGameBoard()
        
    def quitGame(self) -> None:
        """Close own GUI and connection to server."""
        self.connection.sendall("quit".encode())
        self.root.quit()
        self.closeConnection()
    

if __name__ == "__main__":
    player2 = Player2()