import socket
from gameboard import BoardClass

# will be the client - ends entire operation when player 1 chooses to stop playing
def main():
    HOST = input("Enter player 2 host name/IP address: ")
    PORT = int(input("Enter player 2 port: "))
    # make option to retry connection if failed connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.connect((HOST, PORT))
        p1_username = input("Enter username: ")
        connection.sendall(p1_username.encode())
        
        p2_username = connection.recv(1024).decode()
        game = BoardClass(p1_username, p2_username)
        
        quit_key = 1
        while quit_key:
            game.printBoard()
            while True:
                try:
                    raw_move = input("Enter move -> x, y: ")
                    temp = raw_move.split(", ")
                    for i in range(2):
                        e = int(temp.pop(0))
                        temp.append(e)
                    if (game.checkValidMove(temp)):
                        break
                    else:
                        print("Invalid move.")
                except ValueError:
                    print("Invalid move.")
            
            # send move and current board state
            full_move: str = raw_move + "split" + game.getBoard()
            connection.sendall(full_move.encode())
            
            # display move that was just sent out
            game.updateGameBoard(1, temp, game.getBoard())
            game.printBoard()
            print("============")
            
            # receive move and new board state from player 2
            p2_move = connection.recv(1024).decode()
            
            # process move from string into tuple(tuple(int), str)
            p2_move = p2_move.split("split")
            temp = p2_move[0].split(", ")
            for i in range(2):
                e = int(temp.pop(0))
                temp.append(e)
            p2_move[0] = tuple(temp)
            
            # update game board with new information
            game.updateGameBoard(2, p2_move[0], p2_move[1])
            
            # case of game ending in someone's win
            winner = game.isWinner()
            if (winner):
                game.printBoard()
                game.updateGamesPlayed()
                print(f"Player {winner} won.")
                connection.sendall(f"Player {winner} Won".encode())
                
                if (winner == 1):
                    game.updateGamesWon(1)
                else:
                    game.updateGamesLost(1)
                    game.updateLastMove(2)
                
                while True:
                    try:                    
                        play_again = input("Play again? y/n: ")
                        if (play_again == "y" or play_again == "Y"):
                            game.resetGameBoard()
                            connection.sendall(b"Play Again")
                            break
                        elif (play_again == "n" or play_again == "N"):
                            connection.sendall(b"Fun Times")
                            game.printStats(1)
                            quit_key = 0
                            break                    
                        raise ValueError
                    
                    except ValueError:
                        print("Invalid Input.")
            
            # check case of tie
            if (game.boardIsFull()):
                game.printBoard()
                game.updateGamesPlayed()
                game.updateGamesTied(1)
                print("Game is a tie.")
                play_again = input("Play again? y/n: ")
                if (play_again == "y"):
                    connection.sendall(b"Play Again")
                    continue
                else:
                    connection.sendall(b"Fun Times")
                    game.printStats(1)
                    break
        

if __name__ == "__main__":
    main()