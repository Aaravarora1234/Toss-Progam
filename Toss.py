import random
while True :
    Choicelist = ["tails", "heads"]
    Userinput = str(input("Enter your choice (Heads/Tails) : ")).lower()
    Randomoutcome = random.choice(Choicelist)
    Validchoicechecker = Userinput in Choicelist
    if Validchoicechecker == True :
        if Userinput == Randomoutcome :
            if (Userinput == "tails"):
                print("Tails. Congratulations you won.")
            elif (Userinput == "heads"):
                print("Heads. Congratulations you won.")
        else :
            if (Userinput == "tails"):
                print("Tails. Better luck next time.")
            elif (Userinput == "heads"):
                print("Heads. Better luck next time.")
        Fuctionlist = ["Y","N"]
        Playagain = str(input("Type 'Y' to Play again or 'N' to exit.")).upper()
        Validfunctionchecker = Playagain in Fuctionlist
        if Validfunctionchecker == True :
            if Playagain == "Y" :
                print("New game started.")
            elif Playagain == "N" :
                print("Game ended by user.")
                break
        else :
            print("Invalid Function.")
    else :
        print("Invalid Function")