import random
import time
size=3

# board=[[""]*size]*size
# board=[
#     ["","","","",""],
#     ["","","","",""],
#     ["","","","",""],
#     ["","","","",""],
#     ["","","","",""]
# ]
board=[["" for x in range(size)]for y in range(size)]
# graph=[[None]*size]*size
# print(graph[1][2])
# graph=[
#     ["","","1"],
#     ["3","1","3"],
#     ["1","3",""]
# ]
# graph=[
#     ["00","01","02"],
#     ["10","11","12"],
#     ["20","21","22"]
# ]
# print(board)

def TurnA():
    x=random.randrange(size)
    y=random.randrange(size)
    if board[x][y] is None or board[x][y] == "":
        board[x][y]="X"
    else:
        TurnA()
def TurnB():
    x=random.randrange(size)
    y=random.randrange(size)

    if board[x][y] is None or board[x][y] == "":
        board[x][y]="O"
    else:
        TurnB()

def draw():
    for i in range(size):
        print(board[i])
     
def WinChek():
    d1counter=0
    d2counter=0
    Condition=False
    for i in range(size):
        # print("i=",i)
        zero=0
        # kebawah
        counter=zero
        if Condition==False:
            for y in range(size):
                # print("kebawah",i,y,Condition)
                c=y+1
                # print("j=",j)
                if y == (size-1) :
                    z=board[0][i]
                else:
                    z=board[c][i]
                if board[y][i] == z and z is not "" and z is not None:
                    # print("true")
                    counter=counter+1
                else:
                    # print("no")
                    counter=counter+0
                if counter==size:
                    z=z
                    Condition=True
                    # print("pemenanganya adalah:",z)
                    break
                else:
                    Condition=Condition
                    # z=None
        else:
            None

        counter=zero
        if Condition==False:
            for x in range(size):
                # print("kesamping",i,x,Condition)
                c=x+1
                # print("j=",j)
                if x == (size-1) :
                    z=board[i][0]
                else:
                    z=board[i][c]
                if board[i][x] == z and z is not "" and z is not None:
                    # print("true")
                    counter=counter+1
                else:
                    # print("no")
                    counter=counter+0
                if counter==size:
                    z=z
                    Condition=True
                    # print("pemenanganya adalah:",z)
                    break
                else:
                    Condition=Condition
                    # z=None
        else:
            None


        if Condition==False:
            # diagonal
            for j in range(size):
                # print("d1",i,j,Condition)
                if i==j:
                    c=j+1
                    if j == (size-1):
                        z=board[0][0]
                    else:
                        z=board[c][c]
                    if board[j][j]==z and z is not "" and z is not None:
                        d1counter=d1counter+1
                    else:
                        d1counter=d1counter+0
                    if d1counter==size: 
                        z=z
                        Condition=True
                        # print("pemenanganya adalah:",z)
                        break
                    else:
                        Condition=Condition
                    # z=None
        else:
            None

        if Condition==False:
            for j in range(size):
                # print("d2",i,j,Condition)
                # print("i=",i,"j=",j)
                if i==i and j == (size-1)-i:
                    # print(i,j)
                    # print(board[i][j]) 
                    if board[i][j]==board[size-1][j]:
                        z=board[0][size-1]
                        # print("z=",z,"z1= 0",size-1)
                    else:
                        z=board[i+1][j-1]
                        # print("z=",z,"z2=",i+1,j-1)
                    if board[i][j]==z and z is not "" and z is not None:
                        # print(z)
                        d2counter=d2counter+1
                    else:
                        d2counter=d2counter+0
                    # print("jumlah",d2counter)
                    if d2counter==size:
                        z=z
                        Condition=True
                        # print("pemenanganya adalah:",z)
                        break
                    else:
                        Condition=Condition
                    # z=None
                else:
                    None
        else:
            None
                    
    return Condition,z
def HumanTurn():
    avaliable=[]
    avaliable2=[]
    # i=0
    # j=0
    for i in range(size):
        for j in range(size):
            if board[i][j] is "" or board[i][j] is None:
                z=[i,j]
                r = str("".join(map(str, z)))
                avaliable.append(r)
                avaliable2.append(z)
            else:
                avaliable=avaliable
    print(avaliable)
    print(len(avaliable))
    humeninput=input()
    # print(humeninput)
    for i in range(len(avaliable)):
        # print("i=",i)
        if str(humeninput) == avaliable[i]:
            # print("sama")
            z=avaliable2[i]
            # print(z)
            # print(z[0])
            # print(z[1])
            if board[z[0]][z[1]] is not "" or board[z[0]][z[1]] is not None:
                board[z[0]][z[1]]="X"
                break
            else:
                print("maaf input yang anda masukkan salah")
        elif i == int(len(avaliable)-1) and str(humeninput) is not avaliable[int(len(avaliable))-1]:
            # print(avaliable[int(len(avaliable)-1)])
            print("maaf input yang anda masukkan salah")
            HumanTurn()
        else:
            # print("Beda")
            None

def Turn():
    timestart=time.time()
    i=1
    # print(board)
    while i < (size*size)+1:
        if i == 1:
            print("board")
            draw()
        else:
            None

        if i%2==1:
            # TurnA()
            HumanTurn()
        else:
            TurnB()
        print("langkah ke- ",i)
        draw()
        Condition,z=WinChek()
        if Condition==True:
            print("Pemenangnya",z)
            break
        elif i == size*size and Condition==False:
            print("tie game")
            break
        else:
            print("\n")
            i=i+1
    timeend=time.time()
    print(timeend-timestart)
    
Turn()