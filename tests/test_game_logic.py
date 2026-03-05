import pytest
from app import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_check_guess_type_error():
    # Test case where guess is an integer and secret is a string
    guess = 10
    secret = "15"

    outcome, message = check_guess(guess, secret)

    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

    # Test case where guess is an integer and secret is a string, but guess is higher
    guess = 20
    secret = "15"

    outcome, message = check_guess(guess, secret)

    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

    # Test case where guess is an integer and secret is a string, and they are equal
    guess = 15
    secret = "15"

    outcome, message = check_guess(guess, secret)

    assert outcome == "Win"
    assert message == "🎉 Correct!"
