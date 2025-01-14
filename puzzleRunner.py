import chess 
import collections
import json
SOURCE = "/home/tomjan/Projects/TCIT/media/database.json"
STATS = "/home/tomjan/Projects/TCIT/data/puzzleStats.json"
with open(SOURCE,"r") as f:
    database = json.load(f)
with open(STATS,"r") as f:
    stats = json.load(f)
board = chess.Board()



def UciToSan(puzzle):
    fen,moves = puzzle
    new_fen = ""
    board.set_fen(fen)
    moves = moves.split()
    ans = ""
    for i,move in enumerate(moves):
        move_obj = chess.Move.from_uci(move)
        ans += board.san(move_obj) + " "
        board.push(move_obj)
        if i == 0:
            new_fen = board.fen()
            ans = ""
    board.set_fen(new_fen)
    return new_fen, ans

def printLocations():
    mp = collections.defaultdict(lambda: [])
    for i in range(64):
        piece = board.piece_at(i)
        if not piece:
            continue
        piece = str(piece)
        remainder = i % 8 
        row = 1 + (i // 8) 
        col = chr(ord('a')+remainder)

        mp[piece].append(f"{col}{row}")
    for key,ll in mp.items():
        ans = f"Black {key.lower()}: " if key.lower() == key else f"White {key.lower()}: "
        for sq in ll:
            ans += sq + ' '
        print(ans)
    print()


def solvePuzzle(moves):
    arr = moves.split()
    idx = 0 
    color = "White" if board.turn else "Black"
    print(f"You are {color}")
    while idx < len(arr):
        guess = input(f"Enter your move: ")
        print()
        if guess == arr[idx]:
            print("Correct Move ")
            print()
        else:
            print(f"Incorrect Move, Correct Solution is {moves} ")
            print()
            return False
        
        idx += 1 
        if idx == len(arr):
            print("Puzzle Over ")
            print()
            break
        print(f"Opponent played {arr[idx]} ")
        print()
        idx += 1 

    return True

def getRatingGroup(rating):
    low = rating//100
    high = low+1
    return f"{low*100}-{high*100}"

def verbalProblem():
    
    done = False
    while not done:
        print("New problem: ")
        print("------------------------")
        rating = stats["rating"]
        ratingid = getRatingGroup(rating)
        puzzles = database[ratingid]["puzzles"]
        location = database[ratingid]["location"]
        database[ratingid]["location"] += 1 # increment location by one so we never see same puzzle 
        puzzle = puzzles[location]
        fen,moves = UciToSan(puzzle)

        print(f"Current rating is {rating}")
        printLocations()
        result = solvePuzzle(moves)
        historyNote = (puzzle[0],puzzle[1],result)
        stats["problem_history"].append(historyNote) # append current puzz to history
        stats["rating"] = rating + 10 if result else rating - 10
        check = input("Would you quit to continue? (Y/n): ")
        done = True if check.lower() == "y" else False
        print()

    # write to jsons    
    with open(SOURCE,"w") as f:
        json.dump(database,f,indent=4)
    with open(STATS,"w") as f:
        json.dump(stats,f,indent=4)









verbalProblem()











