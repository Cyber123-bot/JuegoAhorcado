import random
import os
import time
from style import *

class HangmanGame:
    # Game constants
    WORDS = [
        "airport", "electric", "elephant", "highway", "education", "orchestra", "audiovisual", "university", 
        "increase", "approach", "opinion", "eagle", "staircase", "occasion", "assistant", "autonomous", "nurse", 
        "article", "incredible", "ideology", "revolutionary", "extraordinary", "communication", "development", 
        "lighting", "consideration", "cooperation", "anticipation", "research", "representation", "provided",
        "concern", "evolving", "inauguration", "experienced", "compensatory", "interesting", 
        "responsibility", "recovery", "opportunities", "individualism", "supervision", "restoration", 
        "celebration", "examination", "personality", "contribution", "articulation", "organization", 
        "legitimation", "amplification", "technology", "introspection", "generalization", "dignification", 
        "verification", "clarification", "approximation", "disintegration", "international", "automation"
    ]
    MAX_ATTEMPTS = 6

    def __init__(self):
        self.chosen_word = random.choice(self.WORDS)
        self.hangman_word = self._initialize_hangman_word()
        self.guessed_letters = 0
        self.letters_used = [self.chosen_word[0]]
        self.attempts = self.MAX_ATTEMPTS

    def _initialize_hangman_word(self):
        """ Initialize hangman_word with underscores for all letters except the first """
        return self.chosen_word[0] + "_" * (len(self.chosen_word) - 1)

    def _print_game_header(self):
        """ Print the game header with current stats """
        print(color.blue + "\tHANGMAN GAME" + color.RESET)
        print(color.yellow + "\nGuessed letters:", color.purple + str(self.guessed_letters) + color.RESET)
        print(color.yellow + "Remaining attempts:", color.purple + str(self.attempts) + color.RESET)
        print(color.yellow + "Word to guess:", color.purple + self.hangman_word.capitalize() + color.RESET)

    def _get_user_input(self):
        """ Get a letter from the user """
        try:
            char_user = input(color.blue + "\nLetter you think might be in the word [/m | /e | /?]: " + color.purple)
        
        # If the user presses Ctrl+C, exit the game
        except KeyboardInterrupt:
            print(color.cyan + "\n\tGoodbye!" + color.RESET)
            exit()
            
        return char_user.lower()

    def _handle_user_input(self, char_user):
        """ Handle the user input and process it """
        # If the user writes /m, show the used letters
        if char_user == "/m":
            print(color.cyan + f"Used letters:", color.purple + str(self.letters_used) + color.RESET)
            input(color.cyan + "\nPress Enter to continue..." + color.RESET)
            return True
        
        # If the user writes /e, exit the game
        elif char_user == "/e":
            print(color.cyan + "\n\tGoodbye!" + color.RESET)
            exit()

        elif char_user == "/?":
            print(color.cyan + "\nYou have to guess the word by providing a letter that you think is in the word.\n" + color.RESET)
            print(color.cyan + "If you want to see the used letters, type: /m.\n" + color.RESET)
            print(color.cyan + "If you want to exit the game, type: /e.\n" + color.RESET)
            input(color.cyan + "Press Enter to continue..." + color.RESET)
            return True

        return False

    def _process_guess(self, char_user):
        """ Process the user's letter guess """
        for letter in char_user:
            # If the letter is not in the used letters list and is a single character
            if letter not in self.letters_used and len(letter) == 1:
                # Add the letter to the used letters list
                self.letters_used.append(letter)

                # If the letter is in the chosen word
                if letter in self.chosen_word:
                    self.guessed_letters += self.chosen_word.count(letter) # Increase the number of guessed letters
                    self._update_hangman_word(letter) # Update the hangman word with the correctly guessed letter
                    print(color.green + f"\n\tThe letter '{letter}' is in the word." + color.RESET)

                    # Print a message to the user when they win and exit
                    if "_" not in self.hangman_word:
                        self._print_won_game()
                        exit()

                else:
                    # Print a message to the user if the letter is not in the word and decrease the number of attempts by 1
                    print(color.red + f"\n\tThe letter '{letter}' is not in the word." + color.RESET)
                    self.attempts -= 1

            else:
                # Print a message to the user if the letter is already in the used letters list
                print(color.red + f"\n\tYou already mentioned the letter '{letter}'.\n\tTo see the used ones, type: /m." + color.RESET)

    def _update_hangman_word(self, letter):
        """ Update the hangman word with the correctly guessed letter """
        self.hangman_word = ''.join([letter if self.chosen_word[i] == letter else self.hangman_word[i] 
                                     for i in range(len(self.chosen_word))])

    def _print_lost_game(self):
        """ Print game status when the user loses """
        # Wait for 0.5 seconds and clear the screen.
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")

        # Print the game header and the unsolved word.
        self._print_game_header()
        print(color.yellow + "Unsolved word:", color.purple + self.chosen_word.capitalize() + color.RESET)
        print(color.red + f"\n\tYou lost!" + color.RESET)

    def _print_won_game(self):
        """ Print game status when the user wins """
        # Wait for 0.5 seconds and clear the screen.
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")

        # Print the game header and a message to the user.
        self._print_game_header()
        print(color.green + "\n\tYou won!" + color.RESET)

    def start_game(self):
        """ Start the Hangman game """
        while self.attempts > 0:
            # Wait for 1 second and clear the screen.
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")

            # Print the game header and get the user input.
            self._print_game_header()
            char_user = self._get_user_input()

            # If the user input is not a letter, handle it.
            if self._handle_user_input(char_user):
                continue

            self._process_guess(char_user) # Process the user's guess

        # If there are no attempts and there are still scripts in the word print the lost game message
        if "_" in self.hangman_word:
            self._print_lost_game()

# Start the Hangman game
if __name__ == "__main__":
    game = HangmanGame()
    game.start_game()
