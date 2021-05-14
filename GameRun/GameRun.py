import random
import GameBoard
import Player
import Computer

#GAMEPLAY DESIGN
Game_Continue = True
Game = GameBoard.Game_Generate()

#Loop Till  Winner Is Found
while (Game_Continue == True):
    #Player Move
    Player.Player_Move(Game)

    #Constant Check For Winning Condition
    if (GameBoard.If_Win(Game) == True):
        print("Player Wins!")
        break
    
    #Computer Move
    Computer.Comp_Move(Game,Computer.Nimsum_Cal(Game))

    #Constant Check For Winning Condition
    if (GameBoard.If_Win(Game) == True):
        print("Computer Win!")
        break
