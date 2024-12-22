# Hangman Game

This project is an implementation of the classic hangman game in Python. The objective of the game is to guess a secret word letter by letter before you run out of attempts.

## How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/Cyber123-bot/HangmanGame.git
   ```
2. Run the `hangman.py` file with Python:
    ```sh
    python hangman.py
    ```
3. The game will show you a word with the first letter revealed and the rest as underscores.
4. Enter a letter that you think is in the word.
5. You have a maximum of 6 attempts to guess the entire word.

## Special Commands

- `/m`: Shows the letters you have already used.
- `/e`: Exit the game.
- `/?`: Shows the game instructions.

## Requirement

- Python 3.x
- random module
- os module
- time module
- style module (must be in the same directory as `hangman.py`)

## Code Structure

- `HangmanGame`: Main class that handles the game logic.
  - `__init__`: Initializes the game.
  - `_initialize_hangman_word`: Initializes the hangman word with underscores.
  - `_print_game_header`: Prints the game header with current statistics.
  - `_get_user_input`: Gets a letter from the user.
  - `_handle_user_input`: Handles special commands from the user.
  - `_process_guess`: Processes the letter guessed by the user.
  - `_update_hangman_word`: Updates the hangman word with the correctly guessed letter.
  - `_print_lost_game`: Prints the game state when the user loses.
  - `_print_won_game`: Prints the game state when the user wins.
  - `start_game`: Starts the game.