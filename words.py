def print_upper_words(word_list, must_start_with=None):
    """Print words from a list in uppercase, based on specified conditions.

    - word_list: a list of words
    - must_start_with: a set of letters; only words starting with these letters will be printed
    """

    for word in word_list:
        if must_start_with is None or word.startswith(tuple(must_start_with)):
            print(word.upper())
