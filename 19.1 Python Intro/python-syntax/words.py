def print_to_upper(words):
    """ Takes a list of words and prints each in uppercase """

    for word in words:
        lower_word = word.lower()
        if lower_word.startswith("e"):
            print(word.upper())

print_to_upper(["hello", "hey", "goodbye", "yo", "yes", "eddie"])