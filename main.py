import piecePaths

# we want to generate a daily training regimen.
# so give the number of blindfold routes to do
# and the number of problems.

ROUTES = 10
PUZZLES = 2


for route in range(10):
    piece,problem= piecePaths.randomRoute(piecePaths.board) 
    sq1,sq2,ans = problem
    print(f"Route number {route +1}")
    print(f"We have a {piece} on {sq1} how many steps to move it to {sq2}?")
    print(f"Answer is {ans}")
