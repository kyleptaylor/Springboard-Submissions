def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    
    new_phrase = {}

    for ltr in phrase:
        new_phrase[ltr] = new_phrase.get(ltr, 0) + 1

    return new_phrase