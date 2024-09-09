### Rock Paper Scissors Lizard Spock ###

import random

print("Rock Paper Scissors Lizard Spock")

print("1) ✊")
print("2) ✋")
print("3) ✌")
print("4) 🦎")
print("5) 🖖")

player = int(input("Pick a number: "))

while player < 1 or player > 5:
    player = int(input("Incorrect number. Enter you number again: "))

computer = random.randint(1, 5)

if player == 1:
    print("You choose: ✊")
elif player == 2:
    print("You choose: ✋")
elif player == 3:
    print("You choose: ✌")
elif player == 4:
    print("You choose: 🦎")
else:
    print("You choose: 🖖")

if computer == 1:
    print("CPU choose: ✊")
elif computer == 2:
    print("CPU choose: ✋")
elif computer == 3:
    print("CPU choose: ✌")
elif computer == 4:
    print("CPU choose: 🦎")
else:
    print("CPU choose: 🖖")

if player == 3 and computer == 2:
    print("The player won!")
elif player == 2 and computer == 1:
    print("The player won!")
elif player == 1 and computer == 4:
    print("The player won!")
elif player == 4 and computer == 5:
    print("The player won!")
elif player == 5 and computer == 3:
    print("The player won!")
elif player == 3 and computer == 4:
    print("The player won!")
elif player == 4 and computer == 2:
    print("The player won!")
elif player == 2 and computer == 5:
    print("The player won!")
elif player == 5 and computer == 1:
    print("The player won!")
elif player == 1 and computer == 3:
    print("The player won!")
elif player == computer:
    print("It's a tie")
else:
    print("The player lost")