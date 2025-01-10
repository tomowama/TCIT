###### THIS READS NEW GAMES, COMPILES STATISTICS FOR THE GAMES AND ADDS THEM TO THE DATABASE
###### READS FROM THE ./data/newGames.pgn file
import chess.pgn
import json

f = open("./data/newGames.pgn")
game = chess.pgn.read_game(f)
output = open("./data/database.pgn", "a")

while game:
    output.write(str(game))
    output.write("\n")
    game = chess.pgn.read_game(f)
    
f.close()
output.close()



def generateStats(game): # here we want to add to the JSON file of stats
    # use stockfish to generate a centipawn lose.
    # get the eco code and extract it 




