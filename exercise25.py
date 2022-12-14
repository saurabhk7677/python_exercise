def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sort the words."""
    return sorted(words)

def print_first_word(words):
    """prints the first word after poping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """print the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first  and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)




# manual call function........

# sentence = "hii i am saurabh i am bad boy"
# words = break_words(sentence)
# print(words)
# sorted_words = sort_words(words)
# print(sorted_words)
# print_first_word(words)
# print_last_word(words)
# print(words)
# print_first_word(sorted_words)
# print_last_word(sorted_words)
# print(sorted_words)
# sorted_words = sort_sentence(sentence)
# print(sorted_words)
# print_first_and_last(sentence)
# print_first_and_last_sorted(sentence)