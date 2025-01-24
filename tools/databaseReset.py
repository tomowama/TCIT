import json

SOURCE = "/home/tomjan/Projects/TCIT/media/database.json"
STATS = "/home/tomjan/Projects/TCIT/data/puzzleStats.json"
with open(SOURCE,"r") as f:
    database = json.load(f)
with open(STATS,"r") as f:
    stats = json.load(f)



for group in database:
    database[group]["location"] = 0

stats["rating"] = 1000
stats["problem_history"] = []


with open(SOURCE,"w") as f:
    json.dump(database,f,indent=4)
with open(STATS,"w") as f:
    json.dump(stats,f,indent=4)

