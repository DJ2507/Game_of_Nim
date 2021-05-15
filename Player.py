import random
import GameBoard
#PLAYER MOVE
def Player_Move(Game):
    GameBoard.Game_Display(Game)
    print()
    Check_Val2 = False
    
    #Loop Used To Ensure Player Inputs Valid Moves
    while (Check_Val2 == False):
        Heap_Chosen = input("Choose Heap: ")
        Pieces_Chosen = input("Choose Number of Pieces To Remove: ")
        
        #Check If Input Is Invalid (E.G. Not Integer)
        try:
            Heap_Chosen = int(Heap_Chosen)
            Pieces_Chosen = int(Pieces_Chosen)
        except ValueError:
            print("Input Error, Try Again")
            Check_Val2 = False
            break
        
        #Check If Input Is Invalid (E.G. Not With Heap and Pieces Range)
        if (Heap_Chosen < 0) or (Heap_Chosen > (len(Game) - 1)) or (Pieces_Chosen < 1) or (Pieces_Chosen > Game[Heap_Chosen]):
            print("Invalid Input, Try Again")
            Check_Val2 = False
        else:
            Game[Heap_Chosen] = Game[Heap_Chosen] - Pieces_Chosen
            Check_Val2 = True

    return Game
