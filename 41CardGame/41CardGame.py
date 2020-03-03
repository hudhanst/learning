import random
def garis(char="-",multiple=10):
        gariss=char*multiple
        return print(gariss)
CardTipe=[
    "♣","♦","♥","♠"
    ]
def CreateCardList(CardTipe=CardTipe):
    CardList=[]
    for w in range(len(CardTipe)):
        for e in range(1,15):
            if e ==14 :
                value=11
            elif e >10:
                value=10
            else:
                value=e

            if e == 11:
                angka="J"
            elif e == 12:
                angka="Q"
            elif e == 13:
                angka="K"
            elif e == 14:
                angka="A"
            else:
                angka=e
            carddata=[angka,CardTipe[w],value]
            CardList.append(carddata)
    return CardList

def SuffelCard(UnshufelCard):
    SuffeledCard=[None for q in range(len(UnshufelCard))]
    for q in range(len(SuffeledCard)):
        w=random.randrange(len(UnshufelCard))
        SuffeledCard[q]=UnshufelCard[w]
        UnshufelCard.remove(UnshufelCard[w])
    return SuffeledCard

class player():
    ALLPLAYER=[]
    def __init__(self,Name):
        self.ALLPLAYER.append(self)
        self.Name=Name
        self.CardHand=[]
        self.SideDeckCard=[]
    
    def DrawCard(self,CardLocation,Amount=1,ShowDrwaedCard=True):
        if CardLocation != self:
            q = -1
        else:
            q=0
        self.CardHand.append(CardLocation[q])
        if ShowDrwaedCard == True:
            print("Drawed Card Are",CardLocation[q])
        else:
            print("Card Are Draw")

        self.RemoveCard(CardLocation,CardLocation[q])
        Amount=Amount-1
        if Amount>0:
            self.DrawCard(CardLocation,Amount,ShowDrwaedCard)
        else:
            return None

    def RemoveCard(self,CardLocation,RemovedCard):
        CardLocation.remove(RemovedCard)
        return None

    def TrowToSideDeck(self,NumberInList):
        for q in range(len(self.CardHand)):
            if q == NumberInList:
                self.SideDeckCard.append(self.CardHand[q])
                self.RemoveCard(self.CardHand,self.CardHand[q])
            else:
                None
        return None
    
    def WhosAreNext(self,CorrentlyPlayer):
        for q in range(len(self.ALLPLAYER)):
            if str(CorrentlyPlayer) == self.ALLPLAYER[q].Name:
                if q == len(self.ALLPLAYER)-1:
                    NextPlayer=self.ALLPLAYER[0]
                    break
                else:
                    NextPlayer=self.ALLPLAYER[q+1]
                    break
            else:
                NextPlayer=None
        return NextPlayer
    def WhosArePrevious(self,CorrentlyPlayer):
        for q in range(len(self.ALLPLAYER)):
            if str(CorrentlyPlayer)== self.ALLPLAYER[q].Name:
                if q == 0:
                    PreviousPlayer=self.ALLPLAYER[len(self.ALLPLAYER)-1]
                    break
                else:
                    PreviousPlayer=self.ALLPLAYER[q-1]
                    break
            else:
                PreviousPlayer=None
        return PreviousPlayer
    def ScoreCheck(self,CardToCheck,CardTipe=CardTipe):
        totalscore=[]
        for q in range(len(CardTipe)):
            score=0
            for w in range(len(CardToCheck)):
                if str(CardTipe[q])==CardToCheck[w][1]:
                    score=score+CardToCheck[w][2]
                else:
                    score=score+0
            totalscore.append(score)
        return totalscore
    def WinCheck(self):
        WinCondition=False
        for q in range(len(CardTipe)):
            score=0
            for w in range(len(self.CardHand)):
                if CardTipe[q]==self.CardHand[w][1]:
                    score=score+self.CardHand[w][2]
                else:
                    score=score+0

                if score==41:
                    WinCondition=True
                    break
                else:
                    None
        return WinCondition

    def PrintingCondition(self,sideshow=True,PreviousPlayer=None):
        if sideshow == False:
            print("Card on Your Hand:\n")
            for q in range(len(self.CardHand)):
                print("no",q,"=",str(self.CardHand[q][0])+str(self.CardHand[q][1]),"|",end="")
            print("\n")
        else:
            print("Card on Your Hand:\n")
            for q in range(len(self.CardHand)):
                print("no",q,"=",str(self.CardHand[q][0])+str(self.CardHand[q][1]),"|",end="")
            if PreviousPlayer != None and len(PreviousPlayer.SideDeckCard)>1:
                print("Card on Your Side: ",PreviousPlayer.SideDeckCard[-1])
            else:
                None
            print("\n")
        return None
    
    def DoS(self,Controler,DeckCard,PreviousPlayer):
        while True:
            try:
                if Controler== "comp":
                    Dos =self.CompDos(PreviousPlayer)
                else:
                    self.PrintingCondition(True)
                    Dos=str(input("Draw Card (D) or take from side (S)??"))
            except ValueError:
                print("input are wrong")
            else:
                if Dos == "D" or Dos == "d":
                    self.DrawCard(DeckCard,1)
                    break
                elif Dos == "S" or Dos == "s":
                    if len(PreviousPlayer.SideDeckCard)<1:
                        print("you cant draw from side deck yet, no card found")
                    else:
                        self.DrawCard(PreviousPlayer.SideDeckCard,1)
                        break
                else:
                    print("input mast be D/d or S/s")
        return None
    def ToC(self,Controler,NextPlayer):
        while True:
            try:
                if Controler=="comp":
                    ToC=self.CompToC()
                else:
                    print("card on your hand: \n")
                    self.PrintingCondition(False)
                    ToC=int(input("Ples Input First Number Card on Your Hand:"))
            except ValueError:
                print("input Must in Number")
            else:
                if ToC>=0 and ToC <=len(self.CardHand)-1:
                    NextPlayer.SideDeckCard.append(self.CardHand[ToC])
                    self.RemoveCard(self.CardHand,self.CardHand[ToC])
                    break
                else:
                    print("Input must betwen 0 and ",len(self.CardHand))
        return None
    def TheBestForMe(self):
        TheBestTipeForMe=None
        TheBestScoreForeMe=0
        TheBestListForMe=[]
        TotalScore=self.ScoreCheck(self.CardHand)
        for q in range(len(TotalScore)):
            if TotalScore[q]>TheBestScoreForeMe:
                TheBestScoreForeMe=TotalScore[q]
                TheBestTipeForMe=CardTipe[q]
            else:
                None
        for w in range(len(self.CardHand)):
            if self.CardHand[w][1]==TheBestTipeForMe:
                TheBestListForMe.append(self.CardHand[w])
            else:
                None
        return TheBestTipeForMe,TheBestListForMe
    def TheWorstForMe(self):
        TheWorstipeForMe=None
        TheWorstScoreForeMe=100
        TheWorstListForMe=[]
        TotalScore=self.ScoreCheck(self.CardHand)
        for q in len(range(TotalScore)):
            if TotalScore[q]<TheWorstScoreForeMe:
                TheWorstScoreForeMe=TotalScore[q]
                TheWorstipeForMe=CardTipe[q]
            else:
                None
        
        for w in len(range(self.CardHand)):
            if self.CardHand[w][1]==TheWorstipeForMe:
                TheWorstListForMe.append(self.CardHand[w])
            else:
                None
        return TheWorstipeForMe,TheWorstListForMe
    def TheBestThrowForMe(self,ListToThrow):
        IsAllTipeSame=False
        TheBestToTrow=None
        for q in range(len(ListToThrow)):
            if all(elm in ListToThrow[q][1] for elm in ListToThrow[0][1]):
                IsAllTipeSame=True
            else:
                None
        if IsAllTipeSame==True:
            lowerscore=100
            for w in range(len(ListToThrow)):
                if lowerscore>ListToThrow[w][2]:
                    lowerscore=ListToThrow[w][2]
                    TheBestToTrow=ListToThrow[w]
                else:
                    None
        else:
            lowerscore=100
            TheWorstipeForMe,TheWorstListForMe=self.TheWorstForMe()
            for e in range(len(TheWorstListForMe)):
                if lowerscore>TheWorstListForMe[e][2]:
                    lowerscore=TheWorstListForMe[e][2]
                    TheBestToTrow=TheWorstListForMe[e]
                else:
                    None
        return TheBestToTrow
    def CompDos(self,PreviousPlayer):
        CompDosCoice=None
        if len(PreviousPlayer.SideDeckCard)<1:
            CompDosCoice="D"
        else:
            TheBestTipeForMe,TheBestListForMe=self.TheBestForMe()
            if PreviousPlayer.SideDeckCard[-1][1]==TheBestTipeForMe:
                if len(TheBestListForMe)>=4:
                    print("len <4")
                    TheBestListForMe.append(PreviousPlayer.SideDeckCard[-1])
                    TheBestToTrow=self.TheBestThrowForMe(TheBestListForMe)
                    if TheBestToTrow==PreviousPlayer.SideDeckCard[-1]:
                        CompDosCoice="D"
                    else:
                        CompDosCoice="S"
                else:
                    CompDosCoice="D"

            else:
                CompDosCoice="D"
        return CompDosCoice
    def CompToC(self):
        ToCCoice=None
        CardToThrow=self.TheBestThrowForMe(self.CardHand)
        for q in range(len(self.CardHand)):
            if self.CardHand[q]==CardToThrow:
                ToCCoice=q
                break
            else:
                None
        return ToCCoice
    
    def Turn(self,DeckCard,Controler="comp"):
        self.PrintingCondition(True)
        NextPlayer=self.WhosAreNext(self.Name)
        PreviousPlayer=self.WhosArePrevious(self.Name)
        self.DoS(Controler,DeckCard,PreviousPlayer)
        garis()
        self.ToC(Controler,NextPlayer)
        WinCondition=self.WinCheck()
        if WinCondition==True:
            winner=self.Name
            
        else:
            winner=None

        return WinCondition,winner

def main():
    # creating games
    CardList=CreateCardList()
    Deck=SuffelCard(CardList)
    # GamesMaxLeng=len(Deck)
    # creating player
    player1=player("player1")
    player2=player("player2")
    player3=player("player3")
    player4=player("player4")
    # Game start
    # for q in range(1,GamesMaxLeng+1):
    q=1
    WinCondition=False
    while WinCondition==False:
        print(q,"- Steps")
        if q == 1:
            for w in range(len(player.ALLPLAYER)):
                player.ALLPLAYER[w].DrawCard(Deck,4,False)
        else:
            None            
        
        if q%4==1:
            # player1.Turn(Deck,"humman")
            WinCondition,winner=player1.Turn(Deck)
        elif q%4==2:
            WinCondition,winner=player2.Turn(Deck)
        elif q%4==3:
            WinCondition,winner=player3.Turn(Deck)
        else:
            WinCondition,winner=player4.Turn(Deck)
        if len(Deck)==0 and WinCondition==False:
            WinCondition="Tie"
            for w in range(len(player.ALLPLAYER)):
                print(player.ALLPLAYER[w].Name, "-",player.ALLPLAYER[w].CardHand)
                break
            else:
                None
        q=q+1
    if WinCondition!=False:
        print(WinCondition,winner)
        for w in range(len(player.ALLPLAYER)):
            print(player.ALLPLAYER[w].Name, "-",player.ALLPLAYER[w].CardHand)
    else:
        None

    return None

if __name__ == "__main__":
    main()

    

