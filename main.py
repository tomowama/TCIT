import piecePaths
import puzzleRunner
# we want to generate a daily training regimen.
# so give the number of blindfold routes to do
# and the number of problems.

ROUTES = 10
PUZZLES = 2


piecePaths.interactiveRoutes(piecePaths.board,ROUTES)
puzzleRunner.interactivePuzzle(PUZZLES)
