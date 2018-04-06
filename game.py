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
    result = input()
