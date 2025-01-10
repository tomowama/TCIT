import csv
import json
RATING_DEV = 84
POPULARITY = 91
INPUT = "/home/tomjan/Projects/Py/TCIT/media/lichess_db_puzzle.csv"
OUTPUT = "/home/tomjan/Projects/Py/TCIT/media/database.json"
database = {}
def putInJson(puzzle):
    # Puzzle is the form (rating,fen,solution)
    def makeRatingGroup(rating):
        low = rating//100
        high = low + 1
        return f"{low*100}-{high*100}"
    
    group = makeRatingGroup(puzzle[0])
    if group in database:
        if len(database[group]["puzzles"]) > 1000:
            return
        database[group]["puzzles"].append((puzzle[1],puzzle[2]))
    else:
        database[group] = {"location":0,"puzzles":[(puzzle[1],puzzle[2])]}


def getProblems():
    f = open(INPUT,'r')
    csv_reader = csv.reader(f)
    for i,row in enumerate(csv_reader):
        if i == 0:
            continue 
        fen = row[1]
        solution = row[2]
        rating = int(row[3])
        rating_dev = int(row[4])
        popularity = int(row[5])
        
        if rating_dev < RATING_DEV and popularity > POPULARITY:
            putInJson((rating,fen,solution))
        if i % 100000 == 0:
            print(i)
    f.close()



getProblems()

for group in database:
    print(group)
    print(len(database[group]))
f = open(OUTPUT,"w")
json.dump(database,f,indent=4)
f.close()


















