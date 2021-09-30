# Input format

# The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. 
# Each cell is denoted by '-' (ascii value: 45). 
# The bot position is denoted by 'm' and the princess position is denoted by 'p'.

# Output format

# Print out the moves you will take to rescue the princess in one go. 
# The moves must be separated by '\n', a newline. 
# The valid moves are LEFT or RIGHT or UP or DOWN.

# Task

# Complete the function displayPathtoPrincess which takes in two parameters - the integer N and the character array grid.
# The grid will be formatted exactly as you see it in the input, so for the sample input the princess is at grid[2][0]. 
# The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the princess. 
# The goal is to reach the princess in as few moves as possible.
# The above sample input is just to help you understand the format. 
# The princess ('p') can be in any one of the four corners.

from random import randrange

FIELDSIZE = 3

EMPTYFIELD = '-'
PRINCESSLOGO = 'p'
WINLOGO = 'p/m'
BOTLOGO = 'm'

RIGHT = "RIGHT"
DOWN = "DOWN"
LEFT = "LEFT"
UP = "UP"

def CreateField(N):
    Field=[[EMPTYFIELD for x in range(N)]for y in range(N)]
    XM = randrange(N)
    YM = randrange(N)
    XP = randrange(N)
    YP = randrange(N)
    print(f'XM={XM}, YM={YM}, XP={XP}, YP={YP}')
    if XM == XP & YM == YP:
        if XM == N-1:
            XM = XM + 1
        else:
            None
    else:
        None
    Field[XM][YM] = BOTLOGO
    Field[XP][YP] = PRINCESSLOGO

    BotCordinate = [XM, YM]
    PrincessCordinate = [XP, YP]
    # print(Field)
    # print(N%2)
    # print(Field[0][1])
    return Field, BotCordinate, PrincessCordinate

def DrawField(ListData, FieldSize):
    for i in range(FieldSize):
        YField = []
        for j in range(FieldSize):
            YField.append(ListData[i][j])
            # print(ListData[i][j])
        print(" | ".join(YField))
        if i != FieldSize-1:
            print(" _ "*FieldSize)
        else:
            None
    return None

def CheckMove(BotCordinate, FieldSize):
    # kanan = i+0, j+1
    canMoveRight = False
    # bawah = i+1, j+0
    canMoveDown = False
    # kiri = i+0, j-1
    canMoveLeft = False
    # atas = i-1, j+0
    canMoveUp = False

    if BotCordinate[1] != FieldSize-1:
        """
        Move to Right
        """
        canMoveRight = True
    else:
        None

    if BotCordinate[0] != FieldSize-1:
        """
        Move to Down
        """
        canMoveDown = True
    else:
        None
    
    if BotCordinate[1] != 0:
        """
        Move to Left
        """
        canMoveLeft = True
    else:
        None
    
    if BotCordinate[0] != 0:
        """
        Move to Up
        """
        canMoveUp = True
    else:
        None

    return canMoveRight, canMoveDown, canMoveLeft,canMoveUp
    # return print(isWin, MoveWin, canMoveRight, canMoveDown, canMoveLeft,canMoveUp)

def WinAnnounced():
    return print("game end")

def Move (Field, BotCordinate, PrincessCordinate, NewMove):
    isWin = False

    NewBotCordinate = None

    OldBotCordinateX = BotCordinate[0]
    OldBotCordinateY = BotCordinate[1]

    NewField = Field[:]
    NewField[OldBotCordinateX][OldBotCordinateY] = EMPTYFIELD

    if NewMove == RIGHT:
        NewBotCordinate = [int(OldBotCordinateX),int(OldBotCordinateY)+1]
    elif NewMove == DOWN:
        NewBotCordinate = [int(OldBotCordinateX)+1,int(OldBotCordinateY)]
    elif NewMove == LEFT:
        NewBotCordinate = [int(OldBotCordinateX),int(OldBotCordinateY)-1]
    elif NewMove == UP:
        NewBotCordinate = [int(OldBotCordinateX)-1,int(OldBotCordinateY)]
    else:
        None
    
    NewField[NewBotCordinate[0]][NewBotCordinate[1]] = BOTLOGO

    if NewBotCordinate[0] == PrincessCordinate[0] and NewBotCordinate[1] == PrincessCordinate[1]:
        NewField[PrincessCordinate[0]][PrincessCordinate[1]] = WINLOGO
        isWin = True
        WinAnnounced()
    else:
        None

    return NewField, NewBotCordinate, isWin

def PlayerInteraction(canMoveRight, canMoveDown, canMoveLeft, canMoveUp):
    PlayerInput = None
    while True:
        try:
            print(" \"W\" for UP \"D\" for RIGHT \"S\" for DOWN \"A\" for LEFT")
            UserInput = input("")
            if UserInput == "W" and canMoveUp or UserInput == "w" and canMoveUp:
                PlayerInput = UP
                break
                # return PlayerInput
            elif UserInput == "D" and canMoveRight or UserInput == "d" and canMoveRight:
                PlayerInput = RIGHT
                break
                # return PlayerInput
            elif UserInput == "S" and canMoveDown or UserInput == "s" and canMoveDown:
                PlayerInput = DOWN
                break
                # return PlayerInput
            elif UserInput == "A" and canMoveLeft or UserInput == "a" and canMoveLeft:
                PlayerInput = LEFT
                # return PlayerInput
                break
            else:
                raise IndexError
        except IndexError:
            print("your press wrong input or input may not avaliable")
            continue
            # PlayerInteraction(canMoveRight, canMoveDown, canMoveLeft,canMoveUp)
    return PlayerInput

Field, BotCordinate, PrincessCordinate = CreateField(FIELDSIZE)
print("First Page:")
DrawField(Field, FIELDSIZE)
isThereAnInput = input("Press Enter to Continue!!!")
GameEnd = False
Step = 0
while GameEnd == False:
    canMoveRight, canMoveDown, canMoveLeft,canMoveUp= CheckMove(BotCordinate, FIELDSIZE)
    PlayerInput = PlayerInteraction(canMoveRight, canMoveDown, canMoveLeft,canMoveUp)
    print(PlayerInput)
    print(f'step {Step}')
    NewField, NewBotCordinate, isWin = Move(Field, BotCordinate, PrincessCordinate, PlayerInput)
    Field = NewField[:]
    BotCordinate = NewBotCordinate[:]
    DrawField(Field, FIELDSIZE)
    GameEnd = isWin
    Step = Step + 1
