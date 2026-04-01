# def add(a, b):
#     return a + b

# if __name__ == "__main__":
#     print(add(2, 3))
import re
from collections import Counter


def clean_text(text: str) -> str:
    """Lowercase and remove special characters."""
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text


def word_count(text: str) -> dict:
    """Return word frequency dictionary."""
    cleaned = clean_text(text)
    words = cleaned.split()
    return dict(Counter(words))


def most_common_word(text: str) -> str:
    """Return the most frequent word."""
    counts = word_count(text)
    return max(counts, key=counts.get)


def average_word_length(text: str) -> float:
    """Return average word length."""
    cleaned = clean_text(text)
    words = cleaned.split()
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)
print(clean_text("Hello World!"))
print(word_count("Hello World! Hello"))
print(most_common_word("Hello World! Hello"))
print(average_word_length("Hello Worldddd!"))

d ={}
x = ('hellos', 'world', 'hello')
for i in range(len(x)):
    print(x[i])