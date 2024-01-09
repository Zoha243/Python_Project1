import random
# Street Fighter
check = True
while check:
    
    p1 = "Player 1"
    p2 = "Player 2"
    p1_Player1s = ["punch", "kick","Haduken","upper kick","block"]
    p2_Player1s = ["punch", "kick","Slam Buster","upper kick","block"]
    p1_life = 100
    p2_life = 100
    stop = True

    while stop:
        Player1 = int(input("Player 1 select your Power\n"))
        Player2 = random.randint(0,4)
        if(Player1 == 0 and Player2 != 4 ):
            print("Player 1 just hit",p1_Player1s[Player1])
            p2_life-=5
        elif Player1 == 1 and Player2 != 4:
            print("Player 1 just hit",p1_Player1s[Player1])
            p2_life-=5
        elif Player1 == 2 and Player2 != 4: 
            print("Player 1 just hit",p1_Player1s[Player1])
            p2_life-=15
        elif Player1 == 3 and Player2 != 4:
            print("Player 1 just hit",p1_Player1s[Player1])
            p2_life-=10
        elif Player1 == 4  or Player2 == 4   :
            print("Player 1 just hit",p1_Player1s[Player1])
            p2_life-=0
        
        if(Player2 == 0 and Player1 != 4):
            print("player 2 life is ",p2_life)
            print("Player 2 just hit",p1_Player1s[Player2])
            p1_life-=5
            print("player 1 life is ",p1_life)
        elif Player2 == 1 and Player1 != 4:
            print("player 2 life is ",p2_life)
            print("Player 2 just hit",p1_Player1s[Player2])
            p1_life-=5
            print("player 1 life is ",p1_life)
        elif Player2 == 2 and Player1 != 4:
            print("player 2 life is ",p2_life)
            print("Player 2 just hit",p1_Player1s[Player2])
            p1_life-=15
            print("player 1 life is ",p1_life)
        elif Player2 == 3 and Player1 != 4:
            print("player 2 life is ",p2_life)
            print("Player 2 just hit",p1_Player1s[Player2])
            p1_life-=10
            print("player 1 life is ",p1_life)
        elif Player2 == 4 or Player1 ==4 :
            print("player 2 life is ",p2_life)
            print("Player 2 just hit",p1_Player1s[Player2])
            p1_life-=0
            print("player 1 life is ",p1_life)
        
        if(p1_life<=0):
            print("Game Over")
            print("Player 2 is winner")
            stop=False
        elif(p2_life<=0):
            print("Game Over")
            print("player 1 is winner")
            stop = False
   
    user=input("Do You want to play Again?Press Y for Yes and N for No\n")
    if user=="Y":
        check = True
    elif user == "N":
        check = False

            
        



