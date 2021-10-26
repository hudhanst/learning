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

FIELDSIZE = 9

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


def CreatePrediction(InitialField, InitialBotCordinate, InitialPrincessCordinate, InitialFieldSize):
    """
    Create a prediction

    Args:
        InitialField ([List]): []
        InitialBotCordinate ([List]): []
        InitialPrincessCordinate ([List]): []
        InitialFieldSize ([Int]): []

    Returns:
        CleanListAllMove [List]: [List of Move, [UP,DOWN,DOWN, etc]]]
    """
    ListAllMove = []
    OptimalMoves = []
    LenOptimalMoves = int(InitialFieldSize**2)
    DONE = 'DONE'
    MAXPOSSIBLEMOVE = 5
    MAXPOSSIBLEPERMUTATION = int(InitialFieldSize**2)

    def Prediction(PredictionData, WorkingNumber, WorkingFieldSize):
        """
        Create a prediction Core, 
        Args:
            PredictionData ([List]): []
            WorkingNumber ([Int]): [Number of "ListAllMove" currently working on]
            WorkingFieldSize ([Int]): []

        Returns:
            None
        """
        WorkingField = PredictionData["Field"][:]
        WorkingMoves = PredictionData["Moves"][:]
        WorkingBotCordinate = PredictionData["BotCordinate"][:]
        WorkingPrincessCordinate = PredictionData["PrincessCordinate"]
        WorkingLastMove = WorkingMoves[-1] if int(
            len(WorkingMoves)) > 0 else False

        def NewMoveBaseOnCounter(N):
            """
            Give NewMove Base on Que Number

            Args:
                N ([Int]): [NUmber of currently que]

            Returns:
                [String]: []
            """
            if N == 0:
                return RIGHT
            elif N == 1:
                return DOWN
            elif N == 2:
                return LEFT
            elif N == 3:
                return UP
            else:
                return DONE

        canMoveRight, canMoveDown, canMoveLeft, canMoveUp = CheckMove(
            WorkingBotCordinate, WorkingFieldSize)

        if WorkingLastMove:
            canMoveRight, canMoveDown, canMoveLeft, canMoveUp = CheckLastMove(
                canMoveRight, canMoveDown, canMoveLeft, canMoveUp, WorkingLastMove)
        else:
            None

        AvaliableMoves = [canMoveRight, canMoveDown, canMoveLeft, canMoveUp]
        BiggestPossibleMove = MAXPOSSIBLEMOVE

        for Counter, AvaMove in enumerate(AvaliableMoves):
            NewMove = NewMoveBaseOnCounter(Counter)
            if AvaMove and NewMove is not DONE and Counter < BiggestPossibleMove:
                AppendData(WorkingField, WorkingBotCordinate,
                           WorkingPrincessCordinate, NewMove, WorkingNumber)
                BiggestPossibleMove = Counter
            elif AvaMove and NewMove is not DONE and Counter > BiggestPossibleMove:
                AddData(WorkingField, WorkingBotCordinate,
                        WorkingPrincessCordinate, NewMove, WorkingMoves)

        return None

    def AppendData(Field, BotCordinate, PrincessCordinate, NewState, PositionNumber):
        """
            Append data to "ListAllMove"

        Args:
            Field ([List]): []
            BotCordinate ([List]): []
            PrincessCordinate ([List]): []
            NewState ([String]): [new move]
            PositionNumber ([Int]): [position of "ListAllMOve" Currently working on]

        Returns:
            None
        """
        WorkingFields = copy.deepcopy(Field)
        WorkingBotCordinate = BotCordinate[:]
        NewFields, NewBotCordinate, isWin = Move(
            WorkingFields, WorkingBotCordinate, PrincessCordinate, NewState)
        ListAllMove[PositionNumber]["Field"] = NewFields[:]

        if isWin:
            ListAllMove[PositionNumber]["BotCordinate"] = PrincessCordinate
            ListAllMove[PositionNumber]["Moves"].append(NewState)
            ListAllMove[PositionNumber]["Moves"].append(DONE)
        else:
            ListAllMove[PositionNumber]["BotCordinate"] = NewBotCordinate[:]
            ListAllMove[PositionNumber]["Moves"].append(NewState)

        return None

    def AddData(Field, BotCordinate, PrincessCordinate, NewState, ListMoves):
        """
        Adding Data to "ListAllMove"

        Args:
            Field ([List]): []
            BotCordinate ([List]): []
            PrincessCordinate ([List]): []
            NewState ([String]): []
            ListMoves ([List]): [All set move before move to make branch]

        Returns:
            None
        """
        WorkingField = copy.deepcopy(Field)
        WorkingBotCordinate = BotCordinate[:]
        WorkingListMoves = ListMoves[:]
        NewField, NewBotCordinate, isWin = Move(
            WorkingField, WorkingBotCordinate, PrincessCordinate, NewState)
        NewAData = {"Field": NewField[:], "Moves": WorkingListMoves[:],
                    "BotCordinate": NewBotCordinate[:], "PrincessCordinate": PrincessCordinate}

        if isWin:
            NewAData["Moves"].append(NewState)
            NewAData["Moves"].append(DONE)
            NewAData["BotCordinate"] = PrincessCordinate
        else:
            NewAData["Moves"].append(NewState)

        ListAllMove.append(NewAData)

        return None

    def FinalClean(ListData, MaxStep):
        """
        Cleaning Data before return to main

        Args:
            ListData ([List]): []
            MaxStep ([Int]): []

        Returns:
            NewData [List]: []
        """
        LowestPossibleMoveSet = MaxStep
        NewData = []
        for x in ListData:
            Moves = x["Moves"]
            if Moves[-1] is DONE:
                Moves.pop(-1)
                LengthOfData = int(len(Moves))
                if LengthOfData < LowestPossibleMoveSet:
                    NewData = []
                    NewData.append(Moves)
                    LowestPossibleMoveSet = LengthOfData
                else:
                    None
            else:
                None

        if len(NewData) < 1:
            return NewData
        else:
            return NewData[0]

    def Optimization(LenMovesList, Comparison):
        """
        if there is already DONE status will change global variable

        Args:
            LenMovesList ([Int]): [Len of Move list -1 bcs DONE are in the list]
            Comparison ([Int]): [Len of OptimalMoves, set to max permutation]

        Returns:
            [Boolean]: [rether change global variable or not]
        """
        if LenMovesList - 1  < Comparison:
            return True
        else:
            return False

    def CheckOptimization(LenMovesList, LenComparison):
        """
        if there is already Optimal solution why should continue, by comparing Moves len and LenOptimalMoves

        Args:
            LenMovesList ([Int]): [Len of Move list]
            Comparison ([Int]): [Len of OptimalMoves, set to max permutation]

        Returns:
            [Boolean]: [rether continue or not]
        """
        if LenMovesList < LenComparison:
            return True
        else: 
            # return True #Un command this if you wanna see all prediction
            return False #Command this if you wanna see all prediction

    print("Make Prediction Pls Wait...")
    FistData = {
        "Field": InitialField[:],
        "Moves": [],
        "BotCordinate": InitialBotCordinate[:],
        "PrincessCordinate": InitialPrincessCordinate,
    }
    ListAllMove.append(FistData)
    InitialData = ListAllMove[0]
    Prediction(InitialData, 0, InitialFieldSize)

    for Counter in range(MAXPOSSIBLEPERMUTATION):
        print(Counter + 1, "Out Of", MAXPOSSIBLEPERMUTATION)
        CurrentAllMovesList = ListAllMove[:]
        for Count, Data in enumerate(CurrentAllMovesList):
            # print("Count", Count, "Data", Data) #See all prediction 
            Moves = Data["Moves"]
            if Moves[-1] is DONE:
                IsOptimization = Optimization(int(len(Moves)), LenOptimalMoves)
                if IsOptimization:
                    OptimalMoves = Moves
                    LenOptimalMoves = int(len(Moves))
                else:
                    None
            else:
                IsContinue = CheckOptimization(int(len(Moves)), LenOptimalMoves)
                if IsContinue:
                    Prediction(Data, Count, InitialFieldSize)
                else:
                    None

    print("Prediction Created")

    CleanListAllMove = FinalClean(ListAllMove, MAXPOSSIBLEPERMUTATION)

    return CleanListAllMove


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
