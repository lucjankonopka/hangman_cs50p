import random

TEXT_WIDTH = 50
HANGMAN_GRAPH = [' ', '_', '_', '_', '_', ' \n',
                 ' ', '|', '/', ' ', '|', ' \n',
                 ' ', '|', ' ', ' ', ' ', ' \n',
                 ' ', '|', ' ', ' ', ' ', ' \n',
                 ' ', '|', ' ', ' ', ' ', ' \n',
                 '/', ' ', '\\', ' ', ' ', ' \n']


# Set default values
def initialize():
    guesses = 6
    # Pick randomly a word from the file and add "_" for each letter
    chosen_word = random.choice(load_words())
    display = ["_" for _ in chosen_word]
    # Create a set for each guessed letter
    user_guesses = set()
    return guesses, display, chosen_word, user_guesses


def main():
    # Initialize the game
    guesses, display, chosen_word, user_guesses = initialize()

    # Welcome message
    print_welcome_message()

    while guesses > 0:
        # Print current status
        print(display_word(chosen_word, display, user_guesses), "\n")
        # Get user input:
        user_guess = input("Guess your letter:\n>>> ").lower()

        # Check user guess validity:
        if not input_check(user_guess, guesses):
            continue

        # Check if user guess is correct:
        guesses = guess_check(user_guess, user_guesses, chosen_word, guesses)

        # Check if user won
        if win_check(chosen_word, user_guesses):
            break

        # Get current status: guesses left or failure
        print(game_status(guesses, chosen_word))


def print_welcome_message() -> None:
    print("-" * TEXT_WIDTH)
    print("Welcome to Hangman!".center(TEXT_WIDTH))
    print("Have fun :)".center(TEXT_WIDTH))
    print("-" * TEXT_WIDTH)


# Open the txt file with example words (words dictionary from scrabble)
def load_words(filename="sowpods.txt") -> list:
    try:
        with open(filename, 'r') as file:
            return [word.strip() for word in file.readlines()]
    except FileNotFoundError as e:
        print("\n", "ERROR: The words database does not exist. Please contact the game provider.", "\n")
        raise e


# Display current status of the word (blank spaces "_" or/and guessed letters)
def display_word(chosen_word, display, user_guesses) -> str:
    print("The word to guess:")

    # Replace blank spaces with correct guessed letters
    for i in range(len(chosen_word)):
        if chosen_word[i] in user_guesses:
            display[i] = chosen_word[i]

    return ' '.join(display)


# Check the user input
def input_check(user_input, guesses) -> bool:
    print("-" * TEXT_WIDTH)
    if not user_input.isalpha() or len(user_input) > 1:
        print("Wrong input! Only single letters will be accepted!")
        print(f"You have {guesses} guesses left!")
        print("-" * TEXT_WIDTH)
        return False
    return True


def win_check(chosen_word, user_guesses) -> bool:
    # Check if the set of guessed letters is a superset of the set of letters in the chosen word
    if set(user_guesses) >= set(chosen_word):
        print("-" * TEXT_WIDTH)
        print("You won!".center(TEXT_WIDTH))
        print(f"The word was \"{chosen_word}\"".center(TEXT_WIDTH))
        print("-" * TEXT_WIDTH)
        return True
    else:
        return False


def game_status(guesses, chosen_word) -> str:
    if guesses == 0:
        output_text = f"{'-' * TEXT_WIDTH}\n"
        output_text += f"You lost!".center(TEXT_WIDTH) + "\n"
        output_text += f"The word was \"{chosen_word}\"".center(TEXT_WIDTH) + "\n"
        output_text += f"{'-' * TEXT_WIDTH}"
        return output_text
    elif guesses == 1:
        return f"You have 1 guess left!\n{'-' * TEXT_WIDTH}"
    else:
        return f"You have {guesses} guesses left!\n{'-' * TEXT_WIDTH}"


def change_hangman_graph(guesses) -> None:
    if guesses == 5:
        HANGMAN_GRAPH[16] = 'O'
    if guesses == 4:
        HANGMAN_GRAPH[22] = '|'
    if guesses == 3:
        HANGMAN_GRAPH[21] = '/'
    if guesses == 2:
        HANGMAN_GRAPH[23] = '\\\n'
    if guesses == 1:
        HANGMAN_GRAPH[27] = '/'
    if guesses == 0:
        HANGMAN_GRAPH[29] = '\\\n'
    print(''.join(HANGMAN_GRAPH))


def guess_check(user_guess, user_guesses, chosen_word, guesses):
    if user_guess in user_guesses:
        print("You've already chosen this letter!")
    else:
        user_guesses.add(user_guess)
        if user_guess in chosen_word:
            print("Correct! The word contains your letter!")
        else:
            guesses -= 1
            change_hangman_graph(guesses)
            print("Incorrect!")
    return guesses


if __name__ == "__main__":
    main()
