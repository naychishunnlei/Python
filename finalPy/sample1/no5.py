# Create a Python function reverse_words(sentence) that takes a string containing words separated by spaces and returns a new string with the words reversed.

def reverse_words(sentence):
    reversed_sentence = ""
    current_word = ""

    for char in sentence:
        if char == " ":
            reversed_sentence = current_word + " " + reversed_sentence
            print(reversed_sentence)
            current_word = ""

        else: 
            current_word += char
            print(current_word)

    reversed_sentence = current_word + " " + reversed_sentence
    return reversed_sentence[:-1]

print(reverse_words("Hello World"))

def reverse(words):
    reversed = ""
    for char in words:
        reversed = char + reversed

    return reversed

print(reverse("Python"))