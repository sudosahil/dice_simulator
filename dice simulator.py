import random
def one():
    print(" ___________")
    print("|           |")
    print("|           |")
    print("|     .     |")
    print("|           |")
    print("|___________|")
def two():
    print(" ___________")
    print("|           |")
    print("|           |")
    print("|   .   .   |")
    print("|           |")
    print("|___________|")
def three():
    print(" ___________")
    print("|           |")
    print("|           |")
    print("|  .  .  .  |")
    print("|           |")
    print("|___________|")
def four():
    print(" ___________")
    print("|           |")
    print("|   .   .   |")
    print("|           |")
    print("|   .   .   |")
    print("|___________|")
def five():
    print(" ___________")
    print("|           |")
    print("|   .   .   |")
    print("|     .     |")
    print("|   .   .   |")
    print("|___________|")
def six():
    print(" ___________")
    print("|           |")
    print("|   . . .   |")
    print("|           |")
    print("|   . . .   |")
    print("|___________|") 

dice = [1,2,3,4,5,6]
while(1<100):
    c = input("ROll? Enter Y or N \n")
    c = c.upper()
    if(c=="Y"):
        n = int(random.choice(dice))
        if(n==1):
            one()
        elif(n==2):
            two()
        elif(n==3):
            three()
        elif(n==4):
            four()
        elif(n==5):
            five()
        elif(n==6):
            six()
    elif(c=="N"):
        print("THANK YOU!")
        break
