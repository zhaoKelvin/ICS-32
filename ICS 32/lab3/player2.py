import socket
from gameboard import BoardClass

# will be the server
def main():
    HOST = input("Enter host name/IP address: ")
    PORT = int(input("Enter port: "))
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as initial_server:
        initial_server.bind((HOST, PORT))
        initial_server.listen()
        
        connection, address = initial_server.accept()
        
        with connection:
            p1_username = connection.recv(1024).decode()
            p2_username = "player2"
            connection.sendall(p2_username.encode())
            game = BoardClass(p1_username, p2_username)
            
            while True:
                # receive move and new board state from player 1
                p1_move = connection.recv(1024).decode()
                
                # case of game ending in someone's win
                if (p1_move == "Player 1 Won" or p1_move == "Player 2 Won"):
                    print(f"Player {p1_move[7]} won.")
                    game.updateGamesPlayed()
                
                    if (p1_move[7] == "1"):
                        game.updateGamesLost(2)  
                    else:
                        game.updateGamesWon(2)
                        game.updateLastMove(2)
                        
                    # player 1 decision to continue/end
                    p1_move = connection.recv(1024).decode()
                    
                if (p1_move == "Play Again"):
                    print(p1_move)
                    game.resetGameBoard()
                    continue
                
                if (p1_move == "Fun Times"):
                    print(p1_move)
                    game.printStats(2)
                    break
                
                # process move from string into a tuple(tuple(int), str)
                p1_move = p1_move.split("split")
                temp = p1_move[0].split(", ")
                for i in range(2):
                    e = int(temp.pop(0))
                    temp.append(e)
                p1_move[0] = tuple(temp)
                game.updateGameBoard(1, p1_move[0], p1_move[1])
                
                # check case of tie
                if (game.boardIsFull()):
                    game.printBoard()
                    game.updateGamesPlayed()
                    game.updateGamesTied(2)
                    print("Game is a tie.")
                    full_move: str = raw_move + "split" + game.getBoard()
                    connection.sendall(full_move.encode())
                    continue
                
                # check case of a win
                winner = game.isWinner()
                if (winner):
                    game.printBoard()
                    #game.updateGamesPlayed()
                    #print(f"Player {winner} won.")
                    full_move: str = raw_move + "split" + game.getBoard()
                    connection.sendall(full_move.encode())
                    continue
                
                # prompt user for new move and check if new move is valid
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
                    except:
                        print("Invalid move.")
                
                # send move and current board state
                full_move: str = raw_move + "split" + game.getBoard()
                connection.sendall(full_move.encode())
                
                # display move that was just sent out
                game.updateGameBoard(2, temp, game.getBoard())
                game.printBoard()
                print("============")
                

if __name__ == "__main__":
    main()