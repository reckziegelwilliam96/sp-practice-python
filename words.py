def print_upper_words(words, must_start_with):
    '''take a list of words and capitalize each letter in each word'''
    for word in words:
        if word[0] == must_start_with[0] or word[0] == must_start_with[1]:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with=["h", "y"])