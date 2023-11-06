# Implement a Python function remove_vowels(word) that removes all vowels from a given word and returns the modified word.

def remove_vowels(word):
    vowels = "aeiouAEIOU"
    words = ""
    for char in word:
        if char not in vowels:
            words += char

    return words

word = "silent"
print(remove_vowels(word))

def remove1(word):
    vowels = "aeiou"
    word = word.lower()
    words = ""

    for char in word:
        if char not in vowels:
            words += char

    return words

print(remove1(word))