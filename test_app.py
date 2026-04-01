# from app import add

# def test_add():
#     assert add(2, 3) == 5
import pytest
from app import clean_text, word_count, most_common_word, average_word_length


sample_text = "Hello world! Hello CI/CD. Welcome to GitHub Actions."


def test_clean_text():
    assert clean_text("Hello!!!") == "hello"


def test_word_count():
    result = word_count(sample_text)
    assert result["hello"] == 2
    assert result["world"] == 1


def test_most_common_word():
    assert most_common_word(sample_text) == "hello"


def test_average_word_length():
    avg = average_word_length("hi hello")
    assert round(avg, 2) == 3.5


def test_empty_input():
    assert average_word_length("") == 0.0