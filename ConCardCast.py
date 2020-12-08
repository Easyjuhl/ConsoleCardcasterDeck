from random import randrange
from utils import CardlistWork

CardcasterLvl = int(input("What is your cardcaster level: "))
HandSizeMax = 1
MajArcPla = 2

if CardcasterLvl > 9:
    MajArcPla = 8
elif CardcasterLvl > 7:
    MajArcPla = 7
elif CardcasterLvl > 5:
    MajArcPla = 6
elif CardcasterLvl > 3:
    MajArcPla = 5
elif CardcasterLvl > 2:
    MajArcPla = 4
elif CardcasterLvl > 1:
    MajArcPla = 3


if CardcasterLvl > 18:
    HandSizeMax = 6
elif CardcasterLvl > 14:
    HandSizeMax = 5
elif CardcasterLvl > 10:
    HandSizeMax = 4
elif CardcasterLvl > 5:
    HandSizeMax = 3
elif CardcasterLvl > 2:
    HandSizeMax = 2

Hand = []
Cardlist = CardlistWork.CardlistReset(CardcasterLvl)

print(*Cardlist, sep=", ")

while True:
    HandSize = len(Hand)
    print("""
    
    To draw a card write: Draw
    To cast a card write: Cast
    To discard a card write: Discard
    To reset write: Reset

    To quit write quit
    """)
    slct = input("Command: ").lower()
    if slct == "draw":
        if HandSize <= HandSizeMax:
            try:
                Cardslct = randrange(len(Cardlist))
            except ValueError:
                print("Out of cards\n")
                print("Your hand:")
                print(*Hand, sep=", ")
                continue
            Hand.append(Cardlist[Cardslct])
            print(Cardlist[Cardslct])
            Cardlist.remove(Cardlist[Cardslct])
            print("Your hand:")
            print(*Hand, sep=", ")
        else:
            print("Your hand is full\nDiscard a card to continue\n")
            print("Your hand:")
            print(*Hand, sep=", ")
            continue
    elif slct == "cast":
        if MajArcPla > 0:
            print(*Hand, sep=", ")
            dis = input("Choose a card to cast: ")
            try:
                Hand.remove(dis)
            except ValueError:
                print("Error: Your input {} is invalid\nRemember to capitalize the correct letters".format(dis))
                continue
            print(*Hand, sep=", ")
    elif slct == "discard":
        print(*Hand, sep=", ")
        dis = input("Choose a card to discard: ")
        try:
            Hand.remove(dis)
        except ValueError:
            print("Error: Your input {} is invalid\nRemember to capitalize the correct letters".format(dis))
            continue
        print(*Hand, sep=", ")
    elif slct == "reset":
        Cardlist = CardlistWork.CardlistReset(CardcasterLvl)
        Hand = []
    elif slct == "quit":
        break
    else:
        print("Error: Invalid input")
