import random
import GameBoard
import Player
import Computer

#GAMEPLAY DESIGN
Continue_Game = True
Game = GameBoard.Generate_Game()

#Loop Till  Winner Is Found
while (Continue_Game == True):
    #Player Move
    Player.Player_Move(Game)

    #Constant Check For Winning Condition
    if (GameBoard.If_Win(Game) == True):
        print("Player Wins!")
        break
    
    #Computer Move
    Computer.Computer_Move(Game, Computer.NimSum_Cal(Game))

    #Constant Check For Winning Condition
    if (GameBoard.If_Win(Game) == True):
        print("Computer Wins!")
        break
