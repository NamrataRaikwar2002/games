import random
print("                    !!!1WHELCOME TO OUR GAME!!! ")
co=["red","blue","black","yellow","green","pink","orange","lightpink","navy blue"]
money=500
i=0
level=1
while i>=0:
    guess_co=random.sample(co,5)
    print(guess_co)
    j=1
    while j<=3:
        guess=input("guess the colour:")
        if guess in guess_co:
            guess_co.remove(guess)
            print("you win the",money,"$","\U0001F917","\U0001F44F")
            print("!!!welcome to",level+1, "level!!")
            money=money+500
            level=level+1
            break
        else:
            print("you have lost the game{}")
            if j+1==4:
                break
            print(j+1,"chance")
        j=j+1
    print("Do you want to proceed/play again!!")
    s= input("enter yes/no:")
    if s=="yes":
        i=i+1
    else:
        print("GAME OVER{0_0}")
        break
print("game over")
