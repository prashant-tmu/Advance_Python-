import random

while True:
    choice = ["stone", "paper", "scissor"]
    bot_take = random.choice(choice)

    user_input = int(input("Enter your choice 1. Stone 2. Paper 3. Scissor: "))

    if user_input > 3 or user_input < 1:
        print("Invalid selection. Exiting game.")
        break
    else:
        user_take = choice[user_input - 1]

    print(f"\nYou chose: {user_take}")
    print(f"Bot chose: {bot_take}")

    if user_take == bot_take:
        print("It's a draw!")
    elif (user_take == "stone" and bot_take == "scissor") or \
         (user_take == "paper" and bot_take == "stone") or \
         (user_take == "scissor" and bot_take == "paper"):
        print("You won!")
    else:
        print("You lose!")

    print("\nLet's play again!\n")
