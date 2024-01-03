from project import load_words, display_word, input_check, win_check, game_status, guess_check
import pytest


def test_load_words_valid_file():
    words = load_words("sowpods.txt")
    assert isinstance(words, list)
    assert len(words) > 0


def test_load_words_no_file():
    with pytest.raises(FileNotFoundError):
        load_words("none.txt")


def test_display_word_example():
    chosen_word = "example"
    display = ["_"] * len(chosen_word)
    user_guesses = ("e", "z", "x")
    assert display_word(chosen_word, display, user_guesses) == "e x _ _ _ _ e"


def test_display_word_none():
    chosen_word = "example"
    display = ["_"] * len(chosen_word)
    user_guesses = ("w", "z", "g")
    assert display_word(chosen_word, display, user_guesses) == "_ _ _ _ _ _ _"


def test_input_check():
    assert input_check("s", 1) == True
    assert input_check("A", 1) == True
    assert input_check("as", 1) == False
    assert input_check("3", 1) == False


def test_win_check():
    assert win_check("cool", {"c", "o", "l"}) == True
    assert win_check("true", {"t", "e", "r", "p", "u"}) == True
    assert win_check("false", {"f", "e", "s", "w", "o"}) == False
    assert win_check("false", {}) == False


def test_game_status():
    text_output_zero = (f"{'-' * 50}" + "\n" + "You lost!".center(50)
                        + "\n" + f"The word was \"{'test'}\"".center(50) + "\n" + f"{'-' * 50}")
    assert game_status(0, "test") == text_output_zero
    text_output_one = f"You have 1 guess left!\n{'-' * 50}"
    assert game_status(1, "test") == text_output_one
    text_output_two = f"You have 2 guesses left!\n{'-' * 50}"
    assert game_status(2, "test") == text_output_two


def test_guess_check():
    assert guess_check("l", {"c", "o", "l"}, "true", 2) == 2
    assert guess_check("r", {"c", "o", "l"}, "true", 2) == 2
    assert guess_check("x", {"c", "o", "l"}, "true", 2) == 1

