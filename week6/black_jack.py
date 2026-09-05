import random


def calculate_score(cards):
    """Calculate the total score of the cards."""
    score = sum(cards)

    return score


def play_blackjack():
    print("""
╔════════════════════════════════════════════════════╗
║                  BLACKJACK                         ║
╚════════════════════════════════════════════════════╝
""")

    # Create a deck
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4

    # Shuffle the cards
    random.shuffle(deck)

    # Deal two cards to player
    player_cards = [deck.pop(), deck.pop()]

    # Deal one card to computer
    computer_cards = [deck.pop()]

    # Player's turn
    while True:

        player_score = calculate_score(player_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check if player goes over 21
        if player_score > 21:
            print(f"\nYour final hand: {player_cards}, final score: {player_score}")
            print(
                f"Computer's final hand: {computer_cards}, "
                f"final score: {calculate_score(computer_cards)}"
            )
            print("You went over. You lose 😭")
            return

        choice = input(
            "Type 'y' to get another card, type 'n' to pass: "
        ).lower()

        if choice == "y":
            new_card = deck.pop()
            player_cards.append(new_card)

        elif choice == "n":
            break

        else:
            print("Please type only 'y' or 'n'.")


    # Computer's turn
    while calculate_score(computer_cards) < 17:
        computer_cards.append(deck.pop())


    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print("\nYour final hand:", player_cards)
    print("Your final score:", player_score)

    print("\nComputer's final hand:", computer_cards)
    print("Computer's final score:", computer_score)

    # Determine winner
    if computer_score > 21:
        print("\nComputer went over. You win! 🎉")

    elif player_score > computer_score:
        print("\nYou win! 🎉")

    elif player_score < computer_score:
        print("\nYou lose 😭")

    else:
        print("\nIt's a draw! 🤝")


# Main game loop
while True:

    answer = input(
        "\nDo you want to play a game of Blackjack? "
        "Type 'y' or 'n': "
    ).lower()

    if answer == "y":
        play_blackjack()

    elif answer == "n":
        print("Thanks for playing Blackjack! 👋")
        break

    else:
        print("Please type 'y' or 'n'.")