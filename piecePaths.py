import random
import collections
## we will move pieces around blindfolded

board = "..........................bwbwbwbw....wbwbwbwb....bwbwbwbw....wbwbwbwb....bwbwbwbw....wbwbwbwb....bwbwbwbw....wbwbwbwb.........................."

def numToSan(board,num): # goes from 0-63 to a san location
    mod = num % 8 
    col = chr(ord("a")+mod)
    row = (num // 8) + 1
    return f"{col}{row}"

def reverseLocator(board,square): # goes from a useable board location to 0-63
    pos = -1
    for i,c in enumerate(board):
        if c != '.':
            pos += 1
        if i == square:
            return pos
def locator(board,square): # goes from 0-63 to a usuable board location
    pos = -1
    for i,c in enumerate(board):
        if c != '.':
            pos += 1
        if pos == square:
            return i,c 

def boardLocToSan(board,loc): # goes from a useable board location to san
    temp = reverseLocator(board,loc)
    return numToSan(board,temp)

def pickSquares(board:str,bishop: bool):
    sq1 = random.randint(0,63)
    loc1,color = locator(board,sq1)
    if bishop:
        sq2 = random.randint(0,63)
        loc2, color2  =locator(board,sq2)
        while color != color2:
            sq2 = random.randint(0,63)
            loc2, color2 = locator(board,sq2)
        return loc1,loc2
    # we are a knight
    sq2 = random.randint(0,63)
    loc2, color2  =locator(board,sq2)
    return loc1,loc2

def getColor(board): # returns the square name and the color useful for guessing the squares
    loc,_ = pickSquares(board,False)
    san = boardLocToSan(board,loc)
    return san,board[loc]

def bishopMove(board,sq):
    moves = [11,13,-11,-13]
    ans = []
    for move in moves:
        if board[sq+move] != '.':
            ans.append(sq+move)
    return ans
    
def bishopsConnect(board,sq1,sq2):
    dq = collections.deque()
    dq.append((sq1,0))
    seen = set()
    while dq:
        sq,depth = dq.popleft()
        if sq == sq2:
            return depth
        if sq in seen:
            continue
        seen.add(sq)
        newSq = bishopMove(board,sq)
        for nsq in newSq:
            dq.append((nsq,depth+1))

def knightMove(board,sq):
    vert = [12,-12]
    horz = [1,-1]
    ans = []
    for v in vert:
        for h in horz:
            newLoc = 2*v + h + sq  
            if board[newLoc] != ".":
                ans.append(newLoc)

    for h in horz:
        for v in vert:
            newLoc = 2*h + v + sq 
            if board[newLoc] != ".":
                ans.append(newLoc)
    return ans



def knightConnect(board,start,end):
    seen = set()

    dq = collections.deque()
    dq.append((start,0))

    while dq:
        loc,depth = dq.popleft()
        if loc == end:
            return depth
        if loc in seen:
            continue
        seen.add(loc)

        newLocs = knightMove(board,loc)

        for nl in newLocs:
            dq.append((nl,depth+1))
        
    return 2000 # error must have occured to get here




def knight(board): # will generate two squares, user will input series of squares to go from on to the next 
    sq1,sq2 = pickSquares(board,False)
    check = knightConnect(board,sq1,sq2) # this give the minimum ammount of moves to reach this square
    sq1,sq2 = boardLocToSan(board,sq1), boardLocToSan(board,sq2)
    return sq1,sq2,check # returns squares and answer

def bishop(board): # will generate two random square, then the user will need to find the closes square connecting both
    sq1,sq2 = pickSquares(board,True)
    check = bishopsConnect(board,sq1,sq2)
    sq1,sq2 = boardLocToSan(board,sq1), boardLocToSan(board,sq2)
    return sq1,sq2,check # returns the squares and  answer


def randomRoute(board):
    choice = random.choice([True,False])
    if choice:
        return "knight",knight(board)
    return "bishop",bishop(board)

def interactiveRoutes(board,limit):
    for route in range(limit):
        piece,problem= randomRoute(board) 
        sq1,sq2,ans = problem
        print(f"Route number {route +1}")
        guess = input(f"We have a {piece} on {sq1} how many steps to move it to {sq2}?\n")
        if int(guess) == int(ans):
            print("Correct!")
        else:
            print(f"Wrong, the correct answer is {ans}")
        print()







