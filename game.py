import random, time, sys

user_score = 0
comp_score = 0
comp_gain = 0
user_gain = 0
track = 0
play_again ='Y'
list = [ "stone", "paper", "scissor"]


print("Welcome to the stone paper scissor game")
print("So let's start")

while play_again == 'Y' or play_again == 'y' :
if track > 0 :
    time.sleep(1)
    print("Result")
    time.sleep(1)
    if user_score > comp_score :
        print("You won")
    else :
        print("You are a loser")
    time.sleep(1)
    print()
    result = input("want to see the score [y/n]")
    if result == 'Y' or result == "Yes" or result == "YES" or result == "yes":
        print("Your score:", user_score, "\nComputer score:", computer_score)

    else:
        print("OK!")
        time.sleep(1)
    print()
    print()
    user_score = 0
    computer_score = 0
    computer_gain = 0
    user_gain = 0
    play_again = input("Want to play again? (Y/N)")
    if play_again == 'N' or play_again == "NO" or play_again == "no":
        break
    else:
        pass
