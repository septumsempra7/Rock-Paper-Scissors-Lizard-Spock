### Rock Paper Scissors ###

import random

print("Rock Paper Scissors")

print("1) ✊")
print("2) ✋")
print("3) ✌")


player = int(input("Pick a number: "))

while player != 1 and player != 2 and player != 3:
    player = int(input("Incorrect number. Enter you number again: "))

computer = random.randint(1, 3)

if player == 1:
    print("You choose: ✊")
elif player == 2:
    print("You choose: ✋")
else:
    print("You choose: ✌")

if computer == 1:
    print("CPU choose: ✊")
elif computer == 2:
    print("CPU choose: ✋")
else:
    print("CPU choose: ✌")

if player == 1 and computer == 3:
    print("The player won!")
elif player == 3 and computer == 2:
    print("The player won!")
elif player == 2 and computer == 1:
    print("The player won!")
elif player == computer:
    print("It's a tie")
else:
    print("The player lost")

