# Create a Python function find_longest_word(list_of_words) that takes a list of words and returns the longest word(s).
# If there are multiple words with the same maximum length, the function should return all of them

def find_longest_word(list_of_words):
    max_length = 0
    words = []
    for word in list_of_words:
        if len(word) > max_length:
            max_length = len(word)
            words = [word]

        elif len(word) == max_length:
            words.append(word)

        else:
            pass

    return words

words = ["abc", "vdkejt", "dfje", "fnejsd"]
print(find_longest_word(words))