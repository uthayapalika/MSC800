import random
import string


class WordGame:

    # Function to get a random word
    def get_random_word(self):
        words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]

        return random.choice(words)

    # Create blanks
    def make_blanks(self, word):
        return ["_" for _ in word]

    # Ask user for a letter
    def prompt_for_letter(self, used_letters):

        while True:
            guess = input("Guess a letter: ").strip().lower()

            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print("Please enter a single A-Z letter.")
                continue

            if guess in used_letters:
                print("You already tried that letter.")
                continue

            return guess

    # Reveal guessed letters
    def reveal_letters(self, word, blanks, letter):

        found_any = False

        for i, ch in enumerate(word):
            if ch == letter and blanks[i] == "_":
                blanks[i] = letter
                found_any = True

        return found_any

    # Check if all blanks are filled
    def all_blanks_filled(self, blanks):
        return "_" not in blanks

    # Main game
    def play_game(self, max_lives=6):

        secret = self.get_random_word()
        blanks = self.make_blanks(secret)

        lives = max_lives
        used = set()

        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(secret)} letters.")
        print(" ".join(blanks))

        while True:

            # Ask user for a letter
            guess = self.prompt_for_letter(used)
            used.add(guess)

            # Check if letter is in word
            if self.reveal_letters(secret, blanks, guess):

                print("\nWell done! Nice job! You found a letter.")
                print(" ".join(blanks))

                # Check if word is complete
                if self.all_blanks_filled(blanks):

                    print("\nCongratulations! You guessed the word!")
                    print(f"Word: {secret}")
                    print("GAME OVER")
                    break

            else:

                lives -= 1

                print(f"\nNope. You lost a life. Lives left: {lives}")
                print(" ".join(blanks))

                # Check lives
                if lives <= 0:

                    print("\nOut of lives!")
                    print(f"The word was: {secret}")
                    print("GAME OVER")
                    break


# Program starts here
if __name__ == "__main__":
    game = WordGame()
    game.play_game()