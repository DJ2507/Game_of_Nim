import random
import GameBoard
#CALCULATE NIM_SUM USING XOR OPERATOR
def Nimsum_Cal(Game):
    sum = 0
    for i in range(len(Game)):
        sum = sum ^ Game[i]
    return sum

#COMPUTER MOVE
def Comp_Move(Game,Nim_Sum):
    print()
    GameBoard.Game_Display(Game)

    # If Player Move Ends with Nim-Sum != 0, Attempt To Make Nim-Sum = 0
    if (Nim_Sum != 0):
        for i in range(len(Game)):
            #Searches For Best Valid Move, If Found Take Move
            if (Game[i]^Nim_Sum < Game[i]):
                #Remove the "nim-sum" number of unit if the piles number is large enought
                print()
                print("Computer Removes",Game[i] - (Game[i] ^ Nim_Sum),"Pieces From Heap",i)
                Game[i] = Game[i] ^ Nim_Sum
                return Game
            
    #If Player Move Ends with Nim-Sum = 0, Make Random Move (Hope Player Makes Error)
    else:
        Random_Heap = random.randint(0,len(Game)-1)
        Game[Random_Heap] -= random.randint(1,Game[Random_Heap])

        return Game
