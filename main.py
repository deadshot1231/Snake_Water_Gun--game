import random

print("Game rules")
print ('''
           Snake = s
             Gun = g
           water = w  
       ''')

code={"s":1,"g":0,"w":-1}
codereverse={1:"snake",0:"gun",-1:"water"}

 
P= "P"

while(P=="P" or P=="p"):
    computer = random.choice([1, 0, -1])

    y= input(" enter your choice : ")

    you=code[y]

    print(f" you chose {codereverse[you]} \n computer chose {codereverse[computer]}")

    if(you==computer):
        print(" game is draw")
    elif((you==1 and computer==0) or (you==0 and computer==-1) or (you==-1 and computer==1)):
        print ("you lose")
    elif((you==1 and computer==-1) or (you==0 and computer==1) or (you==-1 and computer==0)):
        print ("you win balle balle")
    else:
        print('something went wrong') 

    P=input(" if you want to replay type P\nwant to quit press any key expect P : ")