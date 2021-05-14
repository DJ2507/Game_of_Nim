import random

def Game_Generate():
    Game = []
    
    #Generate Random Number of Heaps Between *2 & 5)
    Heaps = random.randint(2,5)
    
    #Generate Random Number of Pieces Per Heap (3 to 8)
    for i in range(Heaps):
        Game.append(random.randint(3,8))

    return Game
    
#DISPLAY GAMEBOARD
def Game_Display(Game):
    for i in range(len(Game)):
        print("Heap",i,":",Game[i])

def If_Win(Game):
    #If 0 Pieces Are Left There Is A Winner
    if sum(Game) == 0: 
        return True
    else : 
        return False
