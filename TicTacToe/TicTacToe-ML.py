import random
# import time
import math
import sys

size=3
itteration=10000

board=[["" for x in range(size)]for y in range(size)]
# def ReNewBoard():
#     board=[["" for x in range(size)]for y in range(size)]
#     return board
# graph=[
#     ["00","01","02"],
#     ["10","11","12"],
#     ["20","21","22"]
# ]
def draw():
    for i in range(size):
        print(board[i])
    return None
# draw()
def AvaliableCondition(board=board,q=0,w=0):
    AvaliableCondition=False
    try:
        if board[q][w]is None or board[q][w]is "":
            AvaliableCondition=True
        else:
            AvaliableCondition=False
    except IndexError:
        AvaliableCondition=False
    return AvaliableCondition
        
def FillBoard(IXoO,BoardCordinat=None):
    if BoardCordinat==None:
        x=random.randrange(size)
        y=random.randrange(size)
    else:
        if int(len(BoardCordinat)) >1:
            x,y=random.choice(BoardCordinat)
        else:
            x=BoardCordinat[0][0]
            y=BoardCordinat[0][1]
    if AvaliableCondition(board,x,y)is True:
        board[x][y]=IXoO
    else:
        FillBoard(IXoO)
    return None
def HumanTurn():
    while True:
        try:
            xcordinat=int(input("masukkan kordinart x!"))
            ycordinat=int(input("masukkan kordinart y!"))
        except ValueError:
            print("input yang anda masukkan harus angka")
        else:
            if xcordinat in range(size) and ycordinat in range(size):
                break
            else:
                print(f"angka yang dimasukkan antara 0-{size}")
    
    if AvaliableCondition(board,xcordinat,ycordinat) is True:
        return [[xcordinat,ycordinat]]
    else:
        print("maaf input yang anda masukkan sudah ter isi")
        HumanTurn()
def ChecPosition():
    AvaliabelSpace=[]
    XPosition=[]
    OPosition=[]
    for q in range(size):
        for w in range(size):
            if AvaliableCondition(board,q,w) is True:
                z=[q,w]
                AvaliabelSpace.append(z)
            elif AvaliableCondition(board,q,w) is False and board[q][w] == "X":
                z=[q,w]
                XPosition.append(z)
            elif AvaliableCondition(board,q,w) is False and board[q][w] == "O":
                z=[q,w]
                OPosition.append(z)
            else:
                None
    return AvaliabelSpace, XPosition, OPosition
def WinStatus(WinCondition=False,Winner=None):
    return WinCondition,Winner

def HorizontalWinCheck():
    HorizontalWinCondition=[]
    for q in range(size):
        x=[]
        for w in range(size):
            z=[q,w]
            x.append(z)
        HorizontalWinCondition.append(x)
    return HorizontalWinCondition

def VerticalWinCheck():
    VerticalWinCondition=[]
    for q in range(size):
        x=[]
        for w in range(size):
            z=[w,q]
            x.append(z)
        VerticalWinCondition.append(x)
    return VerticalWinCondition

def DiagonalLeftSideWinCheck():
    DiagonalLeftSideWinCondition=[]
    for q in range(size):
        for w in range(size):
            if q==w:
                z=[q,w]
                DiagonalLeftSideWinCondition.append(z)
            else:
                None
    return [DiagonalLeftSideWinCondition]
def DiagonalRightSideWinCheck():
    DiagonalRightSideWinCondition=[]
    for q in range(size):
        for w in range(size):
            if w == (size-1)-q:
                z=[q,w]
                DiagonalRightSideWinCondition.append(z)
            else:
                None
    return [DiagonalRightSideWinCondition]

def WinCheck(XPosition, OPosition, HorizontalWinCondition, VerticalWinCondition, DiagonalLeftSideWinCheck, DiagonalRightSideWinCondition):
    WinCondition,Winner=WinStatus()
    for q in range(size):
        if all(elm in XPosition for elm in HorizontalWinCondition[q]) or all(elm in XPosition for elm in VerticalWinCondition[q]) or all(elm in XPosition for elm in DiagonalLeftSideWinCheck[0]) or all(elm in XPosition for elm in DiagonalRightSideWinCondition[0]):
            WinCondition,Winner=WinStatus(True,"X")
            break
        elif all(elm in OPosition for elm in HorizontalWinCondition[q]) or all(elm in OPosition for elm in VerticalWinCondition[q]) or all(elm in OPosition for elm in DiagonalLeftSideWinCheck[0]) or all(elm in OPosition for elm in DiagonalRightSideWinCondition[0]):
            WinCondition,Winner=WinStatus(True,"O")
            break
        else:
            WinCondition=WinCondition
    return WinCondition,Winner

def TryToTie(TheyCondition,WinParameter,SpaceFilledbyOpponent,SpaceNotFilledbyOpponent):
    # print(WinParameter)
    for q in range(int(len(WinParameter))):
        FilledbyOpponent=[w for w in WinParameter[q] if w in TheyCondition]
        NotFilledbyOpponent=[w for w in WinParameter[q] if w not in TheyCondition]
        
        SpaceFilledbyOpponent.append(FilledbyOpponent)
        SpaceNotFilledbyOpponent.append(NotFilledbyOpponent)
    return SpaceFilledbyOpponent,SpaceNotFilledbyOpponent
def TryToWin(OurPosition,WinParameter,SpaceFilledbyUstoWin,AvaliabelSpace,OpponentPosition):
    for q in range(int(len(WinParameter))):
        if len([w for w in WinParameter[q] if w in OpponentPosition])>0:
            FilledbyUstoWin=[]
        else:
            FilledbyUstoWin=[w for w in WinParameter[q] if w not in OurPosition and w in AvaliabelSpace]
        SpaceFilledbyUstoWin.append(FilledbyUstoWin)
    return SpaceFilledbyUstoWin
def KomputerTurn(OpponentPosition,OurPosition,AvaliabelSpace,HorizontalWinCondition,VerticalWinCondition,DiagonalLeftSideWinCondition,DiagonalRightSideWinCondition):
    IsWin=False
    IsTie=False
    BoardWinCondition=[
        HorizontalWinCondition,VerticalWinCondition,DiagonalLeftSideWinCondition,DiagonalRightSideWinCondition
    ]
    SpaceFilledbyOpponent=[]
    SpaceNotFilledbyOpponent=[]
    SpaceFilledbyUstoWin=[]

    for e in range(int(len(BoardWinCondition))):
        TryToWin(OurPosition,BoardWinCondition[e],SpaceFilledbyUstoWin,AvaliabelSpace,OpponentPosition)
    # print("SpaceFilledbyUstoWin",SpaceFilledbyUstoWin)
    for r in range(int(len(SpaceFilledbyUstoWin))):
        LenghtofUs=int(len(SpaceFilledbyUstoWin[r]))
        if LenghtofUs >0 and LenghtofUs < (size-(math.ceil(size*20/100))):
            WinCoisenMove=[t for t in SpaceFilledbyUstoWin[r] if t in AvaliabelSpace]
            # print("WinCoisenMove",WinCoisenMove)
            IsWin=True
            break

    if IsWin==False:
        for q in range(int(len(BoardWinCondition))):
            TryToTie(OpponentPosition,BoardWinCondition[q],SpaceFilledbyOpponent,SpaceNotFilledbyOpponent)
        # print("SpaceFilledbyOpponent",SpaceFilledbyOpponent)
        for w in range(int(len(SpaceFilledbyOpponent))):
            LenghtofOpponent=int(len(SpaceFilledbyOpponent[w]))
            # print("LenghtofOpponent",LenghtofOpponent)
            if LenghtofOpponent == size-(math.ceil(size*20/100)):
                TieCoisenMove=[e for e in SpaceNotFilledbyOpponent[w] if e in AvaliabelSpace]
                if int(len(TieCoisenMove))>0:
                    # print("TieCoisenMove",TieCoisenMove)
                    IsTie=True
                    break
                else:
                    None
            else:
                None
        else:
            None
    # print("IsWin",IsWin)       
    # print("IsTie",IsTie)       
    if IsWin==True:
        return WinCoisenMove
    elif IsTie==True:
        return TieCoisenMove
    else:
        return None
def Main(XTurn="human",OTurn="komp"):
    # board=[["" for x in range(size)]for y in range(size)]
    HorizontalWinCondition=HorizontalWinCheck()
    VerticalWinCondition=VerticalWinCheck()
    DiagonalLeftSideWinCondition=DiagonalLeftSideWinCheck()
    DiagonalRightSideWinCondition=DiagonalRightSideWinCheck()
    
    for q in range ((size*size)+1):
        AvaliabelSpace,XPosition, OPosition=ChecPosition()
        WinCondition, Winner=WinCheck(XPosition, OPosition, HorizontalWinCondition, VerticalWinCondition, DiagonalLeftSideWinCondition, DiagonalRightSideWinCondition)    
        if WinCondition==True:
            break
        elif q==(size*size) and WinCondition==False:
            print("tie game")
            draw()
            print("----")
            break
        else:
            print(f"langkah ke{q+1}")
            draw()
            print("lokasi yang tersedia adalah",AvaliabelSpace)    
            if q%2==0:
                if XTurn=="human":
                    XCoiseCordinate=HumanTurn()
                elif XTurn=="comp":
                    XCoiseCordinate=KomputerTurn(OPosition,XPosition,AvaliabelSpace,HorizontalWinCondition,VerticalWinCondition,DiagonalLeftSideWinCondition,DiagonalRightSideWinCondition)
                else:
                    XCoiseCordinate=None
                print("komputer X memilih",XCoiseCordinate)
                FillBoard("X",XCoiseCordinate)
            else:
                if OTurn=="komp":
                    OCoiseCordinate=KomputerTurn(XPosition,OPosition,AvaliabelSpace,HorizontalWinCondition,VerticalWinCondition,DiagonalLeftSideWinCondition,DiagonalRightSideWinCondition)
                elif OTurn=="comp":
                    OCoiseCordinate=KomputerTurn(XPosition,OPosition,AvaliabelSpace,HorizontalWinCondition,VerticalWinCondition,DiagonalLeftSideWinCondition,DiagonalRightSideWinCondition)
                else:
                    OCoiseCordinate=None
                print("komputer O memilih",OCoiseCordinate)
                FillBoard("O",OCoiseCordinate)
        draw()    
    return Winner

if __name__=="__main__":
    AllWinner=[]
    tiecounter=0
    xcounter=0
    ocounter=0
    
    for it in range(itteration):
        # Main(None,None)
        print("game",it)
        win=Main("comp","comp")
        print("pemengannya",win)
        Winner=[it,win]
        AllWinner.append(Winner)
        board=[["" for x in range(size)]for y in range(size)]
        sys.getrecursionlimit()
    print(AllWinner)
    for q,hasil in enumerate(AllWinner):
        if hasil[1] == None:
            tiecounter=tiecounter+1
        elif hasil[1] == "X":
            xcounter=xcounter+1
        elif hasil[1] == "O":
            ocounter=ocounter+1
        else:
            None
    print(f'jumalh game ={itteration} X menang ={(xcounter*100)/(itteration*100)}% O menang ={(ocounter*100)/(itteration*100)}% hasil imbang ={(tiecounter*100)/(itteration*100)}%')