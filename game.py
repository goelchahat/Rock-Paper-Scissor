import random, time, sys

user_score = 0
computer_score = 0
computer_gain = 0
user_gain = 0
track = 0
play_again = 'Y'
developed = ["Developed ", " By"]
developer = ['J', 'A', 'M', 'E', 'S', ' ', 'G', 'E', 'O', 'R', 'G', 'E']
list = ["stone", "paper", "scissor"]


print("Welcome to the stone paper scissor game!")

print("So let's start!")

while play_again == 'Y' or play_again == 'y':
    if track > 0:
        time.sleep(1)
        print("Result")
        time.sleep(1)
        print()
        print()
        if user_score > computer_score:
            print("Great work ", name, " you won!")
        else:
            print("You are the looser ", name, ". Better luck next time:)")
        time.sleep(1)
        print()
        result = input("Want to see the scores? (Y/N)")
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

    name = input("Kindly input your name:")
    if name == "":
        print("Name required!")
    for i in range(100):
        print("\n")
    while user_gain < 4 and computer_gain < 4:
        track += 1
        user_choice = input("Input whether stone, paper or scissor: ")
        computer_choice = random.choice(list)
        if user_choice == "stone" or user_choice == "paper" or user_choice == "scissor":
            if user_choice == "stone":
                if computer_choice == "stone":
                    pass
                elif computer_choice == "paper":
                    computer_score += 1
                    computer_gain += 1
                    user_gain -= 1
                    user_score -= 1
                else:
                    user_score += 1
                    user_gain += 1
                    computer_gain -= 1
                    computer_score -= 1
            elif user_choice == "paper":
                if computer_choice == "stone":
                    user_score += 1
                    computer_score -= 1
                    computer_gain -= 1
                    user_gain += 1
                elif computer_choice == "paper":
                    pass
                else:
                    user_score -= 1
                    computer_score += 1
                    user_gain -= 1
                    computer_gain += 1
            else:
                if computer_choice == "stone":
                    user_score -= 1
                    computer_score += 1
                    user_gain -= 1
                    computer_gain += 1
                elif computer_choice == "paper":
                    computer_score -= 1
                    user_score += 1
                    computer_gain -= 1
                    user_gain += 1
                else:
                    pass
            print()
            print("Your input is", user_choice, " and computer input is", computer_choice)
            print()
            print("Your score:", user_score, " and computer score:", computer_score)
            print()
            print("Your gain is", user_gain, " and computer gain is", computer_gain)
            print()
            time.sleep(2)
            for i in range(20):
                print("\n")
        else:
            print("Invalid option given!")
            print()
            print()

for i in range(100):
    print("\n")

for i in range(100):
    print("\n")
time.sleep(1)
print("Thank you for trying it out ", name, "!")
print()
print()
for i in developed:
    print(i, end=" ")
    time.sleep(0.5)
print()
for i in developer:
    print(i, end=" ")
    time.sleep(0.4)