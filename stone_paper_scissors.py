# stone paper scissors Game
import random

username = input("Enter your name: ")
user_score = input("Enter your choice Stone, Paper, Scissors): ")
computer_score = random.randint(1, 4)
choice = {
    "Stone" : "1",
    "Paper" : "2",
    "Scissors" : "3",
    1 : "stone",
    2 : "paper",
    3 : "scissors"
}

print("Welcome to the Stone Paper Scissors Game, " + username + "!")
if computer_score == 1 and user_score == "Paper":
    print("Computer chooses " + choice[1])
    print("User chooses " + choice[2])
    print(username + " wins the game!")
elif computer_score == 1 and user_score == "Scissors":
    print("Computer chooses " + choice[1])
    print("User chooses " + choice[3])
    print("Computer wins the game!")
elif computer_score == 2 and user_score == "Stone":
    print("Computer chooses " + choice[2])
    print("User chooses " + choice[1])
    print("Computer wins the game!")
elif computer_score == 2 and user_score == "Scissors":
    print("Computer chooses " + choice[2])
    print("User chooses " + choice[3])
    print(username + " wins the game!")
elif computer_score == 3 and user_score == "Stone":
    print("Computer chooses " + choice[3])
    print("User chooses " + choice[1])
    print(username + " wins the game!")
elif computer_score == 3 and user_score == "Paper":
    print("Computer chooses " + choice[3])
    print("User chooses " + choice[2])
    print("Computer wins the game!")
elif computer_score == user_score:    
    print("Computer chooses " + choice[computer_score])
    print("User chooses " + choice[computer_score])
    print("It's a tie!")
else:
    print("Computer chooses " + choice[computer_score])
    print("User chooses " + user_score)
    print("Invalid input. Please enter Stone, Paper, or Scissors.")