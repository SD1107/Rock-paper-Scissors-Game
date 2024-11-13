#rock paper scissors game
import random
print("                   **********ROCK PAPER GAME**********")
game=["rock","paper","scissors"]
user_input=int(input("Please input your choice . Press 0 for rock, 1 for paper and 2 for scissors\n"))
comp_input=random.randint(0,2)
if 0<=user_input<=2:
    print(f"You chose {game[user_input]}")
    print(f"Computer chose {game[comp_input]}")
    if user_input==0:
        if comp_input==2:
            print("You win!")
        elif user_input>comp_input:
            print("You Win!")
        elif comp_input>user_input:
            print("Computer wins!")
        elif comp_input==user_input:
            print("Match is draw!")
    elif comp_input==0:
        if user_input==2:
            print("Computer wins!")
        elif user_input>comp_input:
            print("You win!")
        elif comp_input>user_input:
            print("Computer wins!")
        elif comp_input==user_input:
            print("Match is draw!")
    else:
        if user_input>comp_input:
            print("You win!")
        elif comp_input>user_input:
            print("Computer wins!")
        elif comp_input==user_input:
            print("Match is draw!")
else:
    print("Wrong Input.Please try again later!")

