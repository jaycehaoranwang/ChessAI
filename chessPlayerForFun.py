from chessPlayer_tree import *
import time
import random
from chessPlayer_evalboard import *
chessBoard=[13,11,12,15,14,12,11,13,
            10,10,10,10,10,10,10,10,
            0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,
            20,20,20,20,20,20,20,20,
            23,21,22,25,24,22,21,23]

#Vanilla Board:
#           [13,11,12,14,15,12,11,13,
#            10,10,10,10,10,10,10,10,
#            0,0,0,0,0,0,0,0,
#            0,0,0,0,0,0,0,0,
#            0,0,0,0,0,0,0,0,
#            0,0,0,0,0,0,0,0,
#            20,20,20,20,20,20,20,20,
#            23,21,22,24,25,22,21,23]

'''
This program utilizes logic and data structures to create an AI that can play EZ Chess at a casual level.
EZ Chess is a version of chess where Castling, En Passant, and pawns moving two squares on their first move is not allowed. This program does not utilize any neural networks and instead implements a pruning algorithm to more efficiently brute-force its way through the game tree and find the best possible move for the specified depth of the game tree. 
'''
def GetPlayerPositions(board,player):
    '''
    Returns a list of the positions of each piece of the specified player if they are on the board
    
    '''
    cBoard=list(board)
    posList=[]
    if player==10:
        for i in range(0,len(cBoard),1):
            if cBoard[i]==13 or cBoard[i]==12 or cBoard[i]==11 or cBoard[i]==10 or cBoard[i]==15 or cBoard[i]==14:
                posList+=[i]
    elif player==20:
        for i in range(0,len(cBoard),1):
            if cBoard[i]==23 or cBoard[i]==22 or cBoard[i]==21 or cBoard[i]==20 or cBoard[i]==25 or cBoard[i]==24:
                posList+=[i]

    return posList

def GetPieceLegalMoves(board, position):
    """
    Gets legal moves for  given piece at the given position.
    """
    pos=position
    cBoard=list(board)
    if cBoard[pos]==10 or cBoard[pos]==20:
        #Checks if the piece at Position is a pawn
        return pawn(cBoard,pos)
    elif cBoard[pos]==13 or cBoard[pos]==23:
        #Checks if piece at position is a rook
        return rook(cBoard,pos)
    #Checks if piece at position is a knight
    elif cBoard[pos]==11 or cBoard[pos]==21:
        return knight(cBoard,pos)
    #Checks if piece at position is a bishop
    elif cBoard[pos]==12 or cBoard[pos]==22:
        return bishop(cBoard,pos)
    #Checks if pos is a queen
    elif cBoard[pos]==14 or cBoard[pos]==24:
        return queen(cBoard,pos)
    #Checks if pos is a king
    elif cBoard[pos]==15 or cBoard[pos]==25:
        return king(cBoard,pos)

'''
All functions frmo here that correspond to the name of a chess piece are used to calculate the legal moves that the specified piece is allowed to make at any given time on the board
'''

def rook(board,pos):
    cBoard=list(board)
    occupiedPos=GetPlayerPositions(board,10)+GetPlayerPositions(board,20)
    legalList=[]
    temp=pos
    breakBool=False
    while True:                             #Finds the pos of revelant right edge
        if (pos+1)%8==0:
            rightEdge=pos
            break
        pos+=1
    pos=temp
    while True:                 #Finds left edge
        if pos%8==0:
            leftEdge=pos
            break
        pos-=1
    pos=temp
    while (pos+8)<63:              #Finds top edge
        pos+=8
    topEdge=pos
    pos=temp
    while (pos-8)>0:           #Finds bottom edge
        pos-=8
    botEdge=pos
    pos=temp
    if (cBoard[pos]-10)==3:                 #Checks if rook is a white rook
        while pos<rightEdge:                #Checks moves to the right
            if breakBool==True:             #Stops Check if there is a piece in the way of the line
                break
            else:
                pos+=1
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=(leftEdge):        #Checks moves to the left
            if breakBool==True:
                break
            else:
                pos-=1
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos<topEdge:         #Checks moves forward
            if breakBool==True:
                break
            else:
                pos+=8
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos>botEdge:
            if breakBool==True:
                break
            else:
                pos-=8
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
    else:                               # If rook is a black rook
        while pos<rightEdge:                #Checks moves to the right
            if breakBool==True:
                break
            else:
                pos+=1
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=(leftEdge):        #Checks moves to the left
            if breakBool==True:
                break
            else:
                pos-=1
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos<topEdge:         #Checks moves forward
            if breakBool==True:
                break
            else:
                pos+=8
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos>botEdge:
            if breakBool==True:
                break
            else:
                pos-=8
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
    return legalList

def bishop(board,pos):
    cBoard=list(board)
    occupiedPos=GetPlayerPositions(board,10)+GetPlayerPositions(board,20)
    temp=pos
    bishopMoveList=[]
    legalList=[]
    breakBool=False
    #Checks bottom and Left Edge
    while True:
        if pos==0 or pos==8 or pos==16 or pos==24 or pos==32 or pos==40 or pos==48 or pos==56:
            botLeftEdge=pos
            break
        elif pos-9<0:
            botLeftEdge=pos
            break
        else:
            pos-=9
    #Checks top and right edge
    pos=temp
    while True:
        if pos==7 or pos==15 or pos==23 or pos==31 or pos==39 or pos==47 or pos==55 or pos==63:
            topRightEdge=pos
            break
        elif pos+9>63:
            topRightEdge=pos
            break
        else:
            pos+=9
    pos=temp
    #Checks bottom and right edge
    while True:
        if pos==7 or pos==15 or pos==23 or pos==31 or pos==39 or pos==47 or pos==55 or pos==63:
            botRightEdge=pos
            break
        elif pos-7<0:
            botRightEdge=pos
            break
        else:
            pos-=7
    pos=temp
    #Checks top and Left Edge
    while True:
        if pos==0 or pos==8 or pos==16 or pos==24 or pos==32 or pos==40 or pos==48 or pos==56:
            topLeftEdge=pos
            break
        elif pos+7>63:
            topLeftEdge=pos
            break
        else:
            pos+=7
    pos=temp
    #Checks if its a white bishop
    if (cBoard[pos]-10)==2:
        while pos!=topRightEdge:                #Checks moves to the Top right
            if breakBool==True:             #Stops Check if there is a piece in the way of the line
                break
            else:
                pos+=9
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=botLeftEdge:        #Checks moves to the bottom left
            if breakBool==True:
                break
            else:
                pos-=9
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=topLeftEdge:        #Checks moves to the Top left
            if breakBool==True:
                break
            else:
                pos+=7
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=botRightEdge:        #Checks moves to the bottom right
            if breakBool==True:
                break
            else:
                pos-=7
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
    #If its a black bishop
    else:
        while pos!=topRightEdge:                #Checks moves to the Top right
            if breakBool==True:             #Stops Check if there is a piece in the way of the line
                break
            else:
                pos+=9
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=botLeftEdge:        #Checks moves to the bottom left
            if breakBool==True:
                break
            else:
                pos-=9
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=topLeftEdge:        #Checks moves to the Top left
            if breakBool==True:
                break
            else:
                pos+=7
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=botRightEdge:        #Checks moves to the bottom right
            if breakBool==True:
                break
            else:
                pos-=7
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
    return legalList

def pawn(board,pos):
    cBoard=list(board)
    occupiedPos = GetPlayerPositions(board,10) + GetPlayerPositions(board,20)
    legalList=[]
    moveAhead=True
    breakBool=False
    if (cBoard[pos]-10)==0:                 #Checks if the pawn is a white pawn
        if pos%8==0:                            #Checks if the Pawn is at the Left Edge of the Board
            for i in occupiedPos:
                if i==(pos+9) and (cBoard[pos+9]-20)>=0: #Checks if Right diagonal is a black piece
                    legalList+=[i]
                elif i==(pos+8):      # Checks if forward position is occupied
                    moveAhead=False
            if moveAhead==True:
                legalList+=[pos+8]
            else:
                moveAhead=True
        elif (pos+1)%8==0:                               #Checks if pawn is at Right edge of board
            for i in occupiedPos:
                if i==(pos+7) and (cBoard[pos+7]-20)>=0: #Checks if Left diagonal is a black piece
                    legalList+=[i]
                elif i==(pos+8):
                    moveAhead=False
            if moveAhead==True:
                legalList+=[pos+8]
            else:
                moveAhead=True
        else:                                        #For pawns at the middle of board
            for i in occupiedPos:
                if i==(pos+7) and (cBoard[pos+7]-20)>=0: #Checks if Left diagonal is a black piece
                    legalList+=[i]
                elif i==(pos+9) and (cBoard[pos+9]-20)>=0: #Checks if Right diagonal is a black piece
                    legalList+=[i]
                elif i==(pos+8):
                    moveAhead=False
            if moveAhead==True:
                legalList+=[pos+8]
            else:
                moveAhead=True

    elif (cBoard[pos]-20)==0:         # Checks if its a black pawn
        if pos%8==0:                            #Checks if the Pawn is at the Left Edge of the Board
            for i in occupiedPos:
                if i==(pos-7) and ((cBoard[pos-7]-10)<10 and (cBoard[pos-7]-10)>=0): #Checks if Right diagonal is a white piece
                    legalList+=[i]
                elif i==(pos-8):
                    moveAhead=False
            if moveAhead==True:
                legalList+=[pos-8]
            else:
                moveAhead=True
        elif (pos+1)%8==0:                               #Checks if pawn is at Right edge of board
            for i in occupiedPos:
                if i==(pos-9) and ((cBoard[pos-9]-10)<10 and (cBoard[pos-9]-10)>=0): #Checks if Left diagonal is a white piece
                    legalList+=[i]
                elif i==(pos-8):
                    moveAhead=False
            if moveAhead==True:
                legalList+=[pos-8]
            else:
                moveAhead=True
        else:                                        #For pawns at the middle of board
            for i in occupiedPos:
                if i==(pos-9) and ((cBoard[pos-9]-10)<10 and (cBoard[pos-9]-10)>=0): #Checks if Left diagonal is a white piece
                    legalList+=[i]
                elif i==(pos-7) and ((cBoard[pos-7]-10)<10 and (cBoard[pos-7]-10)>=0): #Checks if Right diagonal is a white piece
                    legalList+=[i]
                elif i==(pos-8):
                    moveAhead=False
            if moveAhead==True:
                legalList+=[pos-8]
            else:
                moveAhead=True
    return legalList

def knight(board,pos):
    cBoard=list(board)
    occupiedPos=GetPlayerPositions(board,10)+GetPlayerPositions(board,20)
    legalList=[]
    moveAhead=True
    breakBool=False
    temp=pos
    #List to check the incrementing positions that a knight can move on the board
    #Special Cases are to prevent spillover to other side of board
    knightIncrementNeutral=[2,5,4,12,4,5,2,0]
    knightIncrementREdge=[7,16,9,0]
    knightIncrementLEdge=[9,16,7,0]
    knightIncrementRInner=[2,5,16,9,2,0]
    knightIncrementLInner=[2,9,16,5,2,0]
    knightIncrement=[]
    LEdgeBool=False
    #Picks the increment list depending on which special case occurs
    if pos==0 or pos==8 or pos==16 or pos==24 or pos==32 or pos==40 or pos==48 or pos==56:
        knightIncrement=list(knightIncrementLEdge)
        LEdgeBool=True
    elif pos==1 or pos==9 or pos==17 or pos==25 or pos==33 or pos==41 or pos==49 or pos==57:
        knightIncrement=list(knightIncrementLInner)
    elif pos==6 or pos==14 or pos==22 or pos==30 or pos==38 or pos==46 or pos==54 or pos==62:
        knightIncrement=list(knightIncrementRInner)
    elif pos==7 or pos==15 or pos==23 or pos==31 or pos==39 or pos==47 or pos==55 or pos==63:
        knightIncrement=list(knightIncrementREdge)
    else:
        knightIncrement=list(knightIncrementNeutral)
    knightMoveList=[]
    #Initial increment is different if knight is on the left edge of board
    if LEdgeBool==True:
        pos=pos-15
    else:
        pos=pos-17
    knightOccupiedBool=False
    #Making a list of all possible moves of a knight
    for i in knightIncrement:
        knightMoveList+=[pos]
        pos+=i
    pos=temp
    #Checks if knight at pos is white
    if cBoard[pos]-10==1:
        #Validating list of all possible moves into legal ones
        for i in knightMoveList:
            if i>0 and i<64:
                for j in occupiedPos:
                    knightOccupiedBool=False
                    if i==j:
                        #Checks if index j is occupied by a white piece
                        if cBoard[j]-20<0:
                            knightOccupiedBool=True
                            break
                if knightOccupiedBool==False:
                    legalList+=[i]
    #Checks if knight at pos is black
    elif cBoard[pos]-20==1:
        #Validating list of all possible moves into legal ones
        for i in knightMoveList:
            if i>0 and i<64:
                knightOccupiedBool=False
                for j in occupiedPos:
                    knightOccupiedBool=False
                    if i==j:
                        #Checks if index j is occupied by a black piece
                        if cBoard[j]-20>=0:
                            knightOccupiedBool=True
                            break
                if knightOccupiedBool==False:
                    legalList+=[i]
    pos=temp
    return legalList

def queen(board,pos):
    cBoard=list(board)
    occupiedPos=GetPlayerPositions(board,10)+GetPlayerPositions(board,20)
    legalList=[]
    temp=pos
    bishopMoveList=[]
    breakBool=False
    while True:
        if pos==0 or pos==8 or pos==16 or pos==24 or pos==32 or pos==40 or pos==48 or pos==56:
            botLeftEdge=pos
            break
        elif pos-9<0:
            botLeftEdge=pos
            break
        else:
            pos-=9
    #Checks top and right edge
    pos=temp
    while True:
        if pos==7 or pos==15 or pos==23 or pos==31 or pos==39 or pos==47 or pos==55 or pos==63:
            topRightEdge=pos
            break
        elif pos+9>63:
            topRightEdge=pos
            break
        else:
            pos+=9
    pos=temp
    #Checks bottom and right edge
    while True:
        if pos==7 or pos==15 or pos==23 or pos==31 or pos==39 or pos==47 or pos==55 or pos==63:
            botRightEdge=pos
            break
        elif pos-7<0:
            botRightEdge=pos
            break
        else:
            pos-=7
    pos=temp
    #Checks top and Left Edge
    while True:
        if pos==0 or pos==8 or pos==16 or pos==24 or pos==32 or pos==40 or pos==48 or pos==56:
            topLeftEdge=pos
            break
        elif pos+7>63:
            topLeftEdge=pos
            break
        else:
            pos+=7
    pos=temp
    while True:                             #Finds the pos of revelant right edge
        if (pos+1)%8==0:
            rightEdge=pos
            break
        pos+=1
    pos=temp
    while True:                 #Finds left edge
        if pos%8==0:
            leftEdge=pos
            break
        pos-=1
    pos=temp
    while (pos+8)<63:              #Finds top edge
        pos+=8
    topEdge=pos
    pos=temp
    while (pos-8)>0:           #Finds bottom edge
        pos-=8
    botEdge=pos
    pos=temp
    #Checks if its a white queen
    if (cBoard[pos]-10)==4:
        while pos!=topRightEdge:                #Checks moves to the Top right
            if breakBool==True:             #Stops Check if there is a piece in the way of the line
                break
            else:
                pos+=9
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=botLeftEdge:        #Checks moves to the bottom left
            if breakBool==True:
                break
            else:
                pos-=9
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=topLeftEdge:        #Checks moves to the Top left
            if breakBool==True:
                break
            else:
                pos+=7
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=botRightEdge:        #Checks moves to the bottom right
            if breakBool==True:
                break
            else:
                pos-=7
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos<rightEdge:                #Checks moves to the right
            if breakBool==True:             #Stops Check if there is a piece in the way of the line
                break
            else:
                pos+=1
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=(leftEdge):        #Checks moves to the left
            if breakBool==True:
                break
            else:
                pos-=1
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos<topEdge:         #Checks moves forward
            if breakBool==True:
                break
            else:
                pos+=8
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos>botEdge:
            if breakBool==True:
                break
            else:
                pos-=8
            for i in occupiedPos:
                if i==pos and (cBoard[i]-20)>=0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
    #If its a black queen
    else:
        while pos!=topRightEdge:                #Checks moves to the Top right
            if breakBool==True:             #Stops Check if there is a piece in the way of the line
                break
            else:
                pos+=9
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=botLeftEdge:        #Checks moves to the bottom left
            if breakBool==True:
                break
            else:
                pos-=9
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=topLeftEdge:        #Checks moves to the Top left
            if breakBool==True:
                break
            else:
                pos+=7
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=botRightEdge:        #Checks moves to the bottom right
            if breakBool==True:
                break
            else:
                pos-=7
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos<rightEdge:                #Checks moves to the right
            if breakBool==True:
                break
            else:
                pos+=1
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos!=(leftEdge):        #Checks moves to the left
            if breakBool==True:
                break
            else:
                pos-=1
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos<topEdge:         #Checks moves forward
            if breakBool==True:
                break
            else:
                pos+=8
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
        while pos>botEdge:
            if breakBool==True:
                break
            else:
                pos-=8
            for i in occupiedPos:
                if i==pos and (cBoard[i]-16)<0:    #Checks if opponent is present
                    legalList+=[i]
                    breakBool=True
                    break
                elif i==pos:
                    breakBool=True
                    break
            if breakBool!=True:
                legalList+=[pos]
        pos=temp
        breakBool=False
    return legalList

def king(board,pos):
    cBoard=list(board)
    occupiedPos=GetPlayerPositions(board,10)+GetPlayerPositions(board,20)
    legalList=[]
    moveAhead=True
    breakBool=False
    LEdgeBool=False
    temp=pos
    kingIncrement=[]
    kingIncrementLEdge=[1,8,7,1,0]
    kingIncrementREdge=[1,7,8,1,0]
    kingIncrementNeutral=[1,1,6,2,6,1,1,0]
    if pos==0 or pos==8 or pos==16 or pos==24 or pos==32 or pos==40 or pos==48 or pos==56:
        kingIncrement=list(kingIncrementLEdge)
        LEdgeBool=True
    elif pos==7 or pos==15 or pos==23 or pos==31 or pos==39 or pos==47 or pos==55 or pos==63:
        kingIncrement=list(kingIncrementREdge)
    else:
        kingIncrement=list(kingIncrementNeutral)
    kingMoveList=[]
    if LEdgeBool==True:
        pos=pos-8
    else:
        pos=pos-9
    #A List of all possible moves by king
    for i in kingIncrement:
        kingMoveList+=[pos]
        pos+=i
    pos=temp
    kingOccupiedBool=False
    #Checks if king at pos is white
    if cBoard[pos]-10==5:
        #Validating list of all possible moves into legal ones
        for i in kingMoveList:
            if i>0 and i<64:
                for j in occupiedPos:
                    kingOccupiedBool=False
                    if i==j:
                        #Checks if index j is occupied by a white piece
                        if cBoard[j]-20<0:
                            kingOccupiedBool=True
                            break
                if kingOccupiedBool==False:
                    legalList+=[i]
    #Checks if king at pos is black
    elif cBoard[pos]-20==5:
        #Validating list of all possible moves into legal ones
        for i in kingMoveList:
            if i>0 and i<64:
                kingOccupiedBool=False
                for j in occupiedPos:
                    kingOccupiedBool=False
                    if i==j:
                        #Checks if index j is occupied by a black piece
                        if cBoard[j]-20>=0:
                            kingOccupiedBool=True
                            break
                if kingOccupiedBool==False:
                    legalList+=[i]
    pos=temp
    return legalList

def IsPositionUnderThreat(board,position,player):
    '''
    Calculates whether the given position is under threat by the opposing player
    '''
    threatenedPos=position
    whiteOppBool=True
    # If player is black, then the opponent is white, else opponent is black
    if player==20:
        whiteOppBool=True
    else:
        whiteOppBool=False
    #Checks if function was called on an empty position
    if board[threatenedPos]==0:
        return False
    #If player is black and opponent is white
    if whiteOppBool==True:
        for i in GetPlayerPositions(board,10):
            for j in GetPieceLegalMoves(board,i):
                if threatenedPos==j:
                    return True
        return False
    #If player is white opponent is black
    else:
        for i in GetPlayerPositions(board,20):
            for j in GetPieceLegalMoves(board,i):
                if threatenedPos==j:
                    return True
        return False

def evaluateBoard(board):
    '''
    Logical function used to compute the strength/how favourable a given board position/state is and returns a float score based on who the current board position is favouring
    
    '''
    kingW=0
    kingB=0
    knightW=0
    knightB=0
    bishopW=0
    bishopB=0
    rookW=0
    rookB=0
    pawnW=0
    pawnB=0
    queenW=0
    queenB=0
    pawnDefB=0
    pawnDefW=0
    for i in range(0,64,1):
        if board[i]==0:
            pass
        elif board[i]==15:
            kingW+=100
        elif board[i]==25:
            kingB+=100
        elif board[i]==10:
            pawnW+=100
            pawnW+=PSTable(10,i)
            #Checks to see if pawn is defending any pieces
            if i%8!=0 or (i+1)%8!=0:
                if ((board[i+9]-16)<0 or (board[i+7]-16<0)) and (board[i+9]!=0 or (board[i+7]!=0)):
                    pawnDefW+=10
        elif board[i]==20:
            pawnB+=100
            pawnB+=PSTable(20,i)
            #Checks to see if pawn is defending any pieces
            if i%8!=0 or (i+1)%8!=0:
                if ((board[i-9]-16)>0 or (board[i-7]-16)>0) and (board[i-9]!=0 or (board[i-7]!=0)):
                    pawnDefB+=10
        elif board[i]==13:
            rookW+=100
        elif board[i]==23:
            rookB+=100
        elif board[i]==12:
            bishopW+=100
            bishopW+=PSTable(12,i)
        elif board[i]==22:
            bishopB+=100
            bishopB+=PSTable(22,i)
        elif board[i]==11:
            knightW+=100
            knightW+=PSTable(11,i)
        elif board[i]==21:
            knightB+=100
            knightB+=PSTable(21,i)
        elif board[i]==14:
            queenW+=100
        elif board[i]==24:
            queenB+=100


    score=2000*(kingW-kingB)+90*(queenW-queenB)+50*(rookW-rookB)+32.5*(bishopW-bishopB)+30*(knightW-knightB)+10*(pawnW-pawnB)+0.3*(pawnDefW-pawnDefB)

    return score


def allLegalMoves(board,player):
    '''
    Returns a list of all the possible legal moves that the given player can make at the given board state
    
    '''
    whitePlayer=True
    moveList=[]
    # If player is black, then the opponent is white, else opponent is black
    if player != 10:
        whitePlayer=False
    #If player is white
    if whitePlayer==True:
        for i in GetPlayerPositions(board,10):
            for j in GetPieceLegalMoves(board,i):
                moveList+=[[i,j]]
        return moveList
    #If player is black
    else:
        for i in GetPlayerPositions(board,20):
            for j in GetPieceLegalMoves(board,i):
                moveList+=[[i,j]]
        return moveList


def makeGameTree(makeGameBoard,depth,player):
    '''
    Creates the general tree that will be uesd to evaluate the best possible move at any given board state. Each node within the tree stores the board state after a candidate move has been made, a 2-list of the move made [from,to], and the score of that board and returns the tree
    
    '''
    argDepth=depth
    if player==10:
        whiteTurn=True
    else:
        whiteTurn=False
    initTree=tree(makeGameBoard)
    makeGameTreeHelp(makeGameBoard,initTree,depth,whiteTurn)
    return initTree

def makeGameTreeHelp(argBoard, argTree, depth, turnBool):
    '''
    The helper function required to recursively insert nodes into the game tree depth-first
    '''
    if depth == 0:
        return True
    else:
        if turnBool == True:
            side = 10  #WHITE
            turnBool = False
        else:
            side = 20  #BLACK
            turnBool = True
        #print('argBoard:')
        #print(argBoard)
        for i in makeMovesOnBoard(argBoard,side):
            children = tree(i)
            makeGameTreeHelp(i[0],children,depth-1,turnBool)
            argTree.AddSuccessor(children)

def makeMovesOnBoard(moveBoard,player):
    boardList=[]
  #  print(moveBoard)
    for j in (allLegalMoves(moveBoard,player)):
        temp=moveBoard.copy()
      #  print(temp)
        temp[j[1]]=temp[j[0]]
        temp[j[0]]=0
        boardList+=[[temp,j]]
    return boardList

def PSTable(piece,Bpos):
    pawnT=[ 0,  0,  0,  0,  0,  0,  0,  0,
    2, 2, 2, 2, 2, 2, 2, 2,
    1, 1, 2, 3, 3, 2, 1, 1,
     0.5,  0.5, 1, 2.7, 2.7, 1,  0.5,  0.5,
     0,  0,  0, 2.5, 2.5,  0,  0,  0,
     0.5, 0.5, 1,2.5,2.5, 1, 0.5,  0.5,
    0,  0,  0,  0,  0,  0,  0,  0,
     0,  0,  0,  0,  0,  0,  0,  0]
    knightT=[ -5,-4,-3,-3,-3,-3,-4,-5,
    -4,-2,  0,  0,  0,  0,-2,-4,
    -3,  0, 0.5, 1, 1, 0.5,  0,-3,
    -3,  0.5, 1, 1.5, 1.5, 1,  0.5,-3,
    -3,  0, 1, 1.5, 1.5, 1,  0,-3,
    -3,  0.5, 1, 1.2, 1.2, 1,  0.5,-3,
    -4,-2,  0,  0.5,  0.5,  0,-2,-4,
    -5,-4,-2,-3,-3,-2,-4,-5]
    bishopT=[    -2,-1,-1,-1,-1,-1,-1,-2,
    -1,  0,  0,  0,  0,  0,  0,-1,
    -1,  0,  0.5, 1, 1,  0.5,  0,-1,
    -1,  0.5,  0.5, 1, 1,  0.5,  0.5,-1,
    -1,  0, 1, 1, 1, 1,  0,-1,
    -1, 1, 1, 1, 1, 1, 1,-1,
    -1,  0.5,  0,  0,  0,  0,  0.5,-1,
    -2,-1,-4,-1,-1,-4,-1,-2]

    if piece==10:
        return pawnT[63-Bpos]
    elif piece==20:
        return pawnT[Bpos]
    elif piece==11:
        return knightT[63-Bpos]
    elif piece==21:
        return knightT[Bpos]
    elif piece==12:
        return bishopT[63-Bpos]
    elif piece==22:
        return bishopT[Bpos]


def minimax(node, depth, isMaximizingPlayer,alpha,beta):
    if depth==0:
        return evaluateBoard((node.getNode())[0][0])
    if isMaximizingPlayer:
        bestVal=-float("inf")
        for i in node.getSuccessors():
            value=minimax(i,depth-1,False,alpha,beta)
            i.addNodeVal(value)
            bestVal=max(bestVal,value)
            alpha=max(alpha,bestVal)
            if beta <= alpha:
                break
        return bestVal
    else:
        bestVal=float("inf")
        for i in node.getSuccessors():
            value=minimax(i,depth-1,True,alpha,beta)
            i.addNodeVal(value)
            bestVal = min(bestVal,value)
            beta = min(beta,bestVal)
            if beta <= alpha:
                break
        return bestVal

def findMove(gameTree,scoreToFind):
    moveList=[]
    move=[]
    for i in gameTree.getFirstLevel():
        if i[1]==scoreToFind:
            moveList+=[i[0][1]]
    #Randomly picks a move if multiple moves have the same score (WILL NEED UPDATING/UPGRADE THE EVALUATOR FUNCTION)
    randMove=random.randint(0,len(moveList)-1)
    #print('moveList:')
    #print(moveList)
    move=list(moveList[randMove])
    return move

def print_board(board):
    b=[0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(len(b)):
            if board[j]==10:
                b[j]='p'
            elif board[j]==11:
                b[j]='n'
            elif board[j]==12:
                b[j]='b'
            elif board[j]==13:
                b[j]='r'
            elif board[j]==14:
                b[j]='q'
            elif board[j]==15:
                b[j]='k'
            elif board[j]==20:
                b[j]='P'
            elif board[j]==21:
                b[j]='N'
            elif board[j]==22:
                b[j]='B'
            elif board[j]==23:
                b[j]='R'
            elif board[j]==24:
                b[j]='Q'
            elif board[j]==25:
                b[j]='K'
            else:
                b[j]=' '
    row_0=b[0:8]
    row_0=' | '.join(str(d) for d in row_0)
    row_1=b[8:16]
    row_1=' | '.join(str(d) for d in row_1)
    row_2=b[16:24]
    row_2=' | '.join(str(d) for d in row_2)
    row_3=b[24:32]
    row_3=' | '.join(str(d) for d in row_3)
    row_4=b[32:40]
    row_4=' | '.join(str(d) for d in row_4)
    row_5=b[40:48]
    row_5=' | '.join(str(d) for d in row_5)
    row_6=b[48:56]
    row_6=' | '.join(str(d) for d in row_6)
    row_7=b[56:64]
    row_7=' | '.join(str(d) for d in row_7)
    filler="-------------------------------"
    print (" "+row_7)
    print (filler)
    print (" "+row_6)
    print (filler)
    print (" "+row_5)
    print (filler)
    print (" "+row_4)
    print (filler)
    print (" "+row_3)
    print (filler)
    print (" "+row_2)
    print (filler)
    print (" "+row_1)
    print (filler)
    print (" "+row_0)
    return True

# Function for playing Chess against the program

def playChess(board):
    gamePlay=True
    sideInput=True
    while sideInput==True:
        aiSide = input('Which side would you like to play as? W/B:')
        if aiSide=='W' or aiSide=='w' or aiSide=='B' or aiSide=='b':
            sideInput=False
        else:
            print('You are not answering the question, try again')
    if aiSide=='W' or aiSide=='w':
        player=20
    elif aiSide=='B' or aiSide=='b':
        player=10
        
    if player==10:
        whiteBool=True
        ai='White'
    else:
        whiteBool=False
        ai='Black'
    print('Hello, my name is ShallowBlue \n and I am the Chess AI made by Jayce')
    print('Today I will be playing with the '+ai+' pieces')
    print('We will be playing EZ Chess (Google if you dont know), so certain rules of chess do not exist \n Major Rules that dont exist: Pawns cannot move two squares, no castling, no enpassent, no pawn promotion')
    print('Please follow the specified move input format as shown or else I may quit (crash)')
    print('Good Luck! :)')
    
    if player==10:
        while gamePlay:
            
            print_board(board)
            start=time.time()
            newTree=makeGameTree(board,4,player)
            score=minimax(newTree,4,whiteBool,-float("inf"),float("inf"))
            end=time.time() 
            elapsed=end-start
            print('elapsed: '+str(round(elapsed,2))+' sec')
            print('Move Made:')
            moveMade=findMove(newTree,score)
            print(str(moveMade[0])+' '+str(moveMade[1]))
            board[moveMade[1]]=board[moveMade[0]]
            board[moveMade[0]]=0 
            
            print_board(board)       
            
            humanPlayer(board)
            
    else:
        while gamePlay:
            print_board(board)
            humanPlayer(board)
            print_board(board)            
            start=time.time()
            newTree=makeGameTree(board,4,player)
            score=minimax(newTree,4,whiteBool,-float("inf"),float("inf"))
            end=time.time() 
            elapsed=end-start
            print('elapsed: '+str(round(elapsed,2))+' sec')
            print('Move Made:')
            moveMade=findMove(newTree,score)
            print(str(moveMade[0])+' '+str(moveMade[1]))
            board[moveMade[1]]=board[moveMade[0]]
            board[moveMade[0]]=0 
    return True

def humanPlayer(boardState):
    s = input('Make a move (pieceLocation)(space)(targetLocation):')
    numbers = list(map(int, s.split()))
    boardState[numbers[1]]=boardState[numbers[0]]
    boardState[numbers[0]]=0
    return boardState

def aiPlayer(board,side,sideBool):
    file=open('game2.txt','a+')
    start=time.time()
    newTree=makeGameTree(board,4,side)
    score=minimax(newTree,4,sideBool,-float("inf"),float("inf"))
    end=time.time()
    elapsed=end-start
    file.write('elapsed: '+str(round(elapsed,2))+' sec\n')
    file.write('Move Made: \n')
    moveMade=findMove(newTree,score)
    file.write(str(moveMade[0])+' '+str(moveMade[1])+'\n')
    board[moveMade[1]]=board[moveMade[0]]
    board[moveMade[0]]=0  
    
    return board

# Function to setup a game where the program plays itself

def ai_VS_ai(board):
    while True:
        file=open('game2.txt','a+')
        file.write('-----White AI s Turn:\n')
        file.close()
        aiPlayer(board,10,True)
        file=open('game2.txt','a+')
        file.write('-----Black AI s Turn:\n')
        file.close()
        aiPlayer(board,20,False)
        file=open('game2.txt','a+')
        file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        file.close()
        whiteKing=False
        blackKing=False
        for i in board:
            if i==15:
                whiteKing=True
            elif i==25:
                blackKing=True
        if whiteKing==True and blackKing==False:
            file=open('game2.txt','a+')
            file.write('*********White Has Won********\n')
            file.close()
            break
        elif whiteKing==False and blackKing==True:
            file=open('game2.txt','a+')
            file.write('*********Black Has Won********\n')
            file.close()
            break
    

playChess(chessBoard)

