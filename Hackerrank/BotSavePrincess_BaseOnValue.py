# Input format

# The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid.
# Each cell is denoted by '-' (ascii value: 45).
# The bot position is denoted by 'm' and the princess position is denoted by 'p'.

# Output format

# Print out the moves you will take to rescue the princess in one go.
# The moves must be separated by '\n', a newline.
# The valid moves are LEFT or RIGHT or UP or DOWN.

# Task

# Complete the function display Path to Princess which takes in two parameters - the integer N and the character array grid.
# The grid will be formatted exactly as you see it in the input, so for the sample input the princess is at grid[2][0].
# The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the princess.
# The goal is to reach the princess in as few moves as possible.
# The above sample input is just to help you understand the format.
# The princess ('p') can be in any one of the four corners.

from random import randrange
import copy
from typing import NoReturn

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
    """
    [Create Field in List]

    Args:
        N ([Int]): [Max Size exp: 3x3 field]

    Returns:
       Field [List]: [X x Y, two dimension]
       BotCordinate [List]: [0,1]
       PrincessCordinate [List]: [0,1]
    """
    Field = [[EMPTYFIELD for x in range(N)]for y in range(N)]
    XM = randrange(N)
    YM = randrange(N)
    XP = randrange(N)
    YP = randrange(N)

    if XM == XP & YM == YP:
        Field, BotCordinate, PrincessCordinate = CreateField(N)
        return Field, BotCordinate, PrincessCordinate
    else:
        None

    Field[XM][YM] = BOTLOGO
    Field[XP][YP] = PRINCESSLOGO

    BotCordinate = [XM, YM]
    PrincessCordinate = [XP, YP]

    return Field, BotCordinate, PrincessCordinate


def DrawField(ListData, FieldSize):
    """
    Draw

    Args:
        ListData ([List]): [Field Condition]
        FieldSize ([Int]): [Global FIELDSIZE]

    Returns:
        None, Print/Draw Field
    """
    for i in range(FieldSize):
        YField = []
        for j in range(FieldSize):
            YField.append(ListData[i][j])
        print(" | ".join(YField))
        if i != FieldSize-1:
            print(" _ "*FieldSize)
        else:
            None
    return None


def CheckMove(BotCordinate, FieldSize):
    """
    check if bot can move right, down, left or up by comparing bot cordinate with border either 0 or fieldsize limit

    Args:
        BotCordinate ([List]): [position of bot]
        FieldSize ([type]): [field size]

    Returns:
        [Boolean]: [right, down, left, up (True or False)]
    """

    canMoveRight = True if BotCordinate[1] != FieldSize-1 else False
    canMoveDown = True if BotCordinate[0] != FieldSize-1 else False
    canMoveLeft = True if BotCordinate[1] != 0 else False
    canMoveUp = True if BotCordinate[0] != 0 else False

    return canMoveRight, canMoveDown, canMoveLeft, canMoveUp


def MoveRight(OldCordinateX, OldCordinateY):
    """
    generate new cordinate after move RIGHT = X,Y+1

    Args:
        OldCordinateX ([Int]): [X Cordinate Before Move]
        OldCordinateY ([Int]): [Y Cordinate Before Move]

    Returns:
        [List]: [New X,Y]
    """
    NewCordinate = [int(OldCordinateX), int(OldCordinateY)+1]
    return NewCordinate


def MoveDown(OldCordinateX, OldCordinateY):
    """
    generate new cordinate after move DOWN = X+1,Y

    Args:
        OldCordinateX ([Int]): [X Cordinate Before Move]
        OldCordinateY ([Int]): [Y Cordinate Before Move]

    Returns:
        [List]: [New X,Y]
    """
    NewCordinate = [int(OldCordinateX)+1, int(OldCordinateY)]
    return NewCordinate


def MoveLeft(OldCordinateX, OldCordinateY):
    """
    generate new cordinate after move LEFT = X,Y-1

    Args:
        OldCordinateX ([Int]): [X Cordinate Before Move]
        OldCordinateY ([Int]): [Y Cordinate Before Move]

    Returns:
        [List]: [New X,Y]
    """
    NewCordinate = [int(OldCordinateX), int(OldCordinateY)-1]
    return NewCordinate


def MoveUp(OldCordinateX, OldCordinateY):
    """
    generate new cordinate after move UP = X-1,Y

    Args:
        OldCordinateX ([Int]): [X Cordinate Before Move]
        OldCordinateY ([Int]): [Y Cordinate Before Move]

    Returns:
        [List]: [New X,Y]
    """
    NewCordinate = [int(OldCordinateX)-1, int(OldCordinateY)]
    return NewCordinate


def CheckLastMove(canMoveRight, canMoveDown, canMoveLeft, canMoveUp, LastMove):
    """
        Create Inverst Status Base on Last Move
        if last move x then x is unavailable

    Args:
        canMoveRight ([Boolean]): []
        canMoveDown ([Boolean]): []
        canMoveLeft ([Boolean]): []
        canMoveUp ([Boolean]): []
        LastMove ([String]): [RIGHT/DOWN/LEFT/UP/DONE]

    Returns:
        [List]: []
    """
    if LastMove == RIGHT:
        canMoveLeft = False
    elif LastMove == DOWN:
        canMoveUp = False
    elif LastMove == LEFT:
        canMoveRight = False
    elif LastMove == UP:
        canMoveDown = False
    else:
        canMoveRight, canMoveDown, canMoveLeft, canMoveUp = False, False, False, False

    return canMoveRight, canMoveDown, canMoveLeft, canMoveUp


def Move(Fields, BotCordinate, PrincessCordinate, NewMove):
    """
        All Move Happend Here
    Args:
        Fields ([List]): [Fields]
        BotCordinate ([List]): [BotCordinate]
        PrincessCordinate ([List]): [PrincessCordinate]
        NewMove ([List]): [RIGHT/DOWN/LEFT/UP]

    Returns:
        NewField ([List]): [NewField]
        NewBotCordinate ([List]): [NewBotCordinate]
        isWin ([Boolean]): [isWin]
    """
    isWin = False

    NewBotCordinate = None

    OldBotCordinateX = BotCordinate[0]
    OldBotCordinateY = BotCordinate[1]

    NewField = Fields[:]
    NewField[OldBotCordinateX][OldBotCordinateY] = EMPTYFIELD

    if NewMove == RIGHT:
        NewBotCordinate = MoveRight(OldBotCordinateX, OldBotCordinateY)
    elif NewMove == DOWN:
        NewBotCordinate = MoveDown(OldBotCordinateX, OldBotCordinateY)
    elif NewMove == LEFT:
        NewBotCordinate = MoveLeft(OldBotCordinateX, OldBotCordinateY)
    elif NewMove == UP:
        NewBotCordinate = MoveUp(OldBotCordinateX, OldBotCordinateY)
    else:
        NewBotCordinate = BotCordinate
        return NewField, NewBotCordinate, isWin

    NewField[NewBotCordinate[0]][NewBotCordinate[1]] = BOTLOGO

    if isWinCheck([NewBotCordinate[0], NewBotCordinate[1]], [PrincessCordinate[0], PrincessCordinate[1]]):
        NewField[PrincessCordinate[0]][PrincessCordinate[1]] = WINLOGO
        isWin = True
    else:
        None

    return NewField[:], NewBotCordinate, isWin


def isWinCheck(BotCordinate, PrincessCordinate):
    """
        Compare Bot and Princess Cordinate
    Args:
        BotCordinate ([List]): [BotCordinate]
        PrincessCordinate ([List]): [PrincessCordinate]

    Returns:
        [Boolean]: [Win Condition base on bot and princess cordinate]
    """
    if BotCordinate[0] == PrincessCordinate[0] and BotCordinate[1] == PrincessCordinate[1]:
        return True
    else:
        return False


def WinAnnounced():
    """
        Print Win if Win
    """
    return print("game end \n")


def CreateCalculatedField(BlankField, BenchCordinate, FieldSize):
    """
        Calculate how much step needed for "BenchCordinate" to ech Cordinate
    Args:
        BlankField ([List]): [Original Position]
        BenchCordinate ([List]): []
        FieldSize ([Int]): []

    Returns:
        NewField [List]: []
    """
    NewField = copy.deepcopy(BlankField)
    for x in range(FieldSize):
        for y in range(FieldSize):
            if NewField[x][y] is EMPTYFIELD:
                NewField[x][y] = int(
                    abs(x-int(BenchCordinate[0]))+abs(y-int(BenchCordinate[1])))
            else:
                None
    return NewField


def CalculatingProbability(OriginalField, FirstField, SecondField, FieldSize):
    """
        create prob score for ech cordinate by divaide ech firstfield and ech secondfield cordinate
    Args:
        OriginalField ([List]): [Actually i don't know why i need this]
        FirstField ([List]): []
        SecondField ([List]): []
        FieldSize ([Int]): []

    Returns:
        NewField [List]: [New field with prob score]
    """
    NewField = copy.deepcopy(OriginalField)
    for x in range(FieldSize):
        for y in range(FieldSize):
            if NewField[x][y] is EMPTYFIELD:
                NewField[x][y] = float(FirstField[x][y]/SecondField[x][y])
            else:
                None
    return NewField


def CreatePrediction(InitialField, InitialBotCordinate, InitialPrincessCordinate, InitialFieldSize):
    """
        Create Prediction

    Args:
        InitialField ([List]): []
        InitialBotCordinate ([List]): []
        InitialPrincessCordinate ([List]): []
        InitialFieldSize ([Int]): []

    Returns:
        BestMoves[List]: []
    """

    BestMoves = []

    def Predict(WorkingProbField, WorkingBotCor, WorkingPrincesCor, WorkingFieldSize):
        """
        Predict base on prob field
        Args:
            WorkingProbField ([List]): []
            WorkingBotCor ([List]): []
            WorkingPrincesCor ([List]): []
            WorkingFieldSize ([Int]): []

        Returns:
            isWin[Boolean]: []
            State[String]: []
        """
        isWin = False
        if isWinCheck(WorkingBotCor, WorkingPrincesCor):
            isWin = True
            return isWin
        else:
            LowestPossibleScore = 0
            AvaliableMoves = [canMoveRight, canMoveDown, canMoveLeft, canMoveUp] = CheckMove(
                WorkingBotCor, WorkingFieldSize)

            for Counter, avamove in enumerate(AvaliableMoves):
                if avamove:
                    if Counter == 0:
                        NewCordinate = MoveRight(
                            WorkingBotCor[0], WorkingBotCor[1])
                        NewState = RIGHT
                    elif Counter == 1:
                        NewCordinate = MoveDown(
                            WorkingBotCor[0], WorkingBotCor[1])
                        NewState = DOWN
                    elif Counter == 2:
                        NewCordinate = MoveLeft(
                            WorkingBotCor[0], WorkingBotCor[1])
                        NewState = LEFT
                    elif Counter == 3:
                        NewCordinate = MoveUp(
                            WorkingBotCor[0], WorkingBotCor[1])
                        NewState = UP
                    else:
                        print(
                            f'someting wrong on "Predict" Counter should not be = {Counter}')

                    ProbScore = WorkingProbField[NewCordinate[0]
                                                 ][NewCordinate[1]]

                    if ProbScore is PRINCESSLOGO:
                        State = NewState
                        isWin = True
                        break
                    elif ProbScore > LowestPossibleScore:
                        LowestPossibleScore = ProbScore
                        State = NewState
                    else:
                        None
                else:
                    None
            return isWin, State

    print("Make Prediction Pls Wait...")

    BotField = CreateCalculatedField(
        InitialField, InitialBotCordinate, InitialFieldSize)
    PrincessField = CreateCalculatedField(
        InitialField, InitialPrincessCordinate, InitialFieldSize)
    ProbabilityField = CalculatingProbability(
        InitialField, BotField, PrincessField, InitialFieldSize)
    # print("BotField",BotField)
    # print("PrincessField",PrincessField)
    # print("ProbabilityField",ProbabilityField)
    BotCordinate = InitialBotCordinate

    for i in range(InitialFieldSize**2):
        print(i+1, "/", InitialFieldSize**2)
        isDone, NewState = Predict(
            ProbabilityField, BotCordinate, InitialPrincessCordinate, InitialFieldSize)
        ProbabilityField[BotCordinate[0]][BotCordinate[1]] = 0
        BestMoves.append(NewState)

        if NewState is RIGHT:
            BotCordinate = MoveRight(BotCordinate[0], BotCordinate[1])
        elif NewState is DOWN:
            BotCordinate = MoveDown(BotCordinate[0], BotCordinate[1])
        elif NewState is LEFT:
            BotCordinate = MoveLeft(BotCordinate[0], BotCordinate[1])
        elif NewState is UP:
            BotCordinate = MoveUp(BotCordinate[0], BotCordinate[1])
        else:
            print(
                f'someting wrong on "CreatePrediction" NewState should not be = {NewState}')

        ProbabilityField[BotCordinate[0]][BotCordinate[1]] = BOTLOGO

        if isDone:
            for remains in range(InitialFieldSize**2 - i):  # Just for aesthetic
                print(i+1+remains, "/", InitialFieldSize**2)

            break

    print("Prediction Created")

    return BestMoves


def main():
    """
        Main
    Returns:
        None
    """
    Field, BotCordinate, PrincessCordinate = CreateField(FIELDSIZE)
    print("Initial Field Position")
    DrawField(Field, FIELDSIZE)
    Prediction = CreatePrediction(
        Field, BotCordinate, PrincessCordinate, FIELDSIZE)

    if Prediction and len(Prediction) > 0:
        Step = 0
        GameEnd = False
        while GameEnd == False:
            BotInput = Prediction[Step]
            print(f'step {Step+1} go {Prediction[Step]}')
            NewField, NewBotCordinate, isWin = Move(
                Field, BotCordinate, PrincessCordinate, BotInput)
            Field = NewField[:]
            BotCordinate = NewBotCordinate[:]
            DrawField(Field, FIELDSIZE)
            GameEnd = isWin

            if GameEnd:
                WinAnnounced()

            Step = Step + 1
    else:
        print("something wrong, there is no prediction")
    return None


main()
# for x in range(10): #TODO DEBUGGING
#     print("main", x)
#     main()
