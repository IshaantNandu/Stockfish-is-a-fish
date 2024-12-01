from stockfish import Stockfish
from random import randrange as rand
import sys

# Initialize Stockfish with your specific path
stockfish = Stockfish(path="/opt/homebrew/Cellar/stockfish/17/bin/stockfish")
stockfish.update_engine_parameters({"Threads": 2, "Minimum Thinking Time": 10})

def board():
    global player
    print(stockfish.get_board_visual(not bool(player)))
def checkelo():
    x:str=input("Elo \n")
    try:
        int(x)  # Try converting the input to an integer
        if int(x) < 1 or int(x) > 3642:
            print("Invalid Elo \n \r Set Elo rating again")
            checkelo()
        else:
            stockfish.set_elo_rating(int(x))
    except ValueError:
        print("Invalid Elo \n \r Set Elo rating again")
        checkelo()
def askMove():
    print("Move")
    if stockfish.is_fen_valid(stockfish.get_fen_position()):
        move:str=input("What's your move?")
        board()
        if stockfish.is_move_correct(move):
            stockfish.make_moves_from_current_position([move])

        else:print("Sorry- invalid move refer to https://www.chess.com/article/view/chess-notation")
    else:mateq()
def mateq():
    checkstat:dict=stockfish.get_evaluation()
    if checkstat['type']=='mate':
        if checkstat['value']<0:
            print("""
♘:Your majesty, your defenses are looking a little pale!\n
♚:Thanks MR Obvious horsey\n
♘:NOBODY calls me horsey \n
♚:Who cares, BTW SAYONARA Whitey boy
                  """)
            sys.exit()
        else:
            print("""
♝:Crissy Crossy Apple Saucy Stale Mate \n
♙:Isn't it a check mate? \n
♔,♖,♕:NANI!!
            """)
            sys.exit()

    else:
        print("Stalemate")
def botmmove():
    if stockfish.is_fen_valid(stockfish.get_fen_position()):
        move:str=stockfish.get_best_move()
        stockfish.make_moves_from_current_position([move])
        board()
        print("Stockfish's move- \n",move)



    else:mateq() 
# Choose player
player:bool=bool(rand(0,3))

# Display the board
board()

#checks elo for stockfish
checkelo()
if bool(player):
    while True:
        askMove()
        botmmove()
else:
    while True:
        botmmove()
        askMove()



