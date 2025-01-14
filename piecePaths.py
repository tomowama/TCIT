import random
import collections
## we will move pieces around blindfolded


board = """
    ............
    ............
    ..bwbwbwbw..
    ..wbwbwbwb..
    ..bwbwbwbw..
    ..wbwbwbwb..
    ..bwbwbwbw..
    ..wbwbwbwb..
    ..bwbwbwbw..
    ..wbwbwbwb..
    ............
    ............
"""


def knight(move): # will generate two squares, user will input series of squares to go from on to the next 
    pass




def bishop(): # will generate two random square, then the user will need to find the closes square connecting both
    pass


def locator(board,square):
    pos = 0
    for i,c in enumerate(board):
        if pos == square:
            return i,c 
        if c != '.':
            pos += 1

def pickSquares(board:str,bishop: bool):
    sq1 = random.randint(0,63)
    if bishop:
        loc1,color = locator(board,sq1)
        sq2 = random.randint(0,63)
        loc2, color2  =locator(board,sq2)
        while color != color2:
            sq2 = random.randint(0,63)
            loc2, color2  =locator(board,sq2)
        return loc1,loc2
    # we are a knight
    sq2 = random.randint(0,63)
    loc2, color2  =locator(board,sq2)
    return loc1,loc2

def bishopMove(board,sq):
    moves = [11,13,-11,-13]
    ans = []
    for move in moves:
        if board[sq+move] != '.':
            ans.append(sq+move)
    return ans
    
def bishopsConnect(sq1,sq2):
    dq = collections.deque()
    dq.append((True,sq1))
    dq.append((False,sq2))
    seen = set()
    while dq:
        num,sq = dq.popleft()
        if (not num, sq) in seen:
            break
        seen.add((num,sq))