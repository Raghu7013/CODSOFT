import random

def RPS():
    player_score = 0
    bot_score = 0
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', or 'scissors'. Type 'q' to quit.")

    while True:
        player_choice = input("\nEnter your choice: ").lower()

        if player_choice == 'q':
            print(f"\nFinal score -> Player: {player_score} || Bot: {bot_score}")
            if player_score > bot_score:
                print("🏆 The winner is YOU!")
            elif bot_score > player_score:
                print("🤖 Winner is the BOT!")
            else:
                print("🤝 It's a tie!")
            break

        if player_choice not in choices:
            print("⚠️ Enter a valid choice: rock, paper, or scissors")
            continue

        bot_choice = random.choice(choices)
        print(f"You chose: {player_choice}")
        print(f"Bot chose: {bot_choice}")

        if player_choice == bot_choice:
            print("😐 It's a tie!")
        elif (player_choice == "rock" and bot_choice == "scissors") or \
             (player_choice == "scissors" and bot_choice == "paper") or \
             (player_choice == "paper" and bot_choice == "rock"):
            player_score += 1
            print("🎉 You win this round!")
        else:
            bot_score += 1
            print("🤖 Bot wins this round!")

RPS()
