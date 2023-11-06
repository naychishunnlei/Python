def freq_counter(list):
    freq = {}

    for item in list:
        if item in freq:
            freq[item] += 1

        else:
            freq[item] = 1

    return freq

list = [1, 2, 1, 1, 3, 4, 2, 5, 3, 2, 3, 4]
print(freq_counter(list))

def word_counter(text):
    words = text.split()
    w = [w.lower() for w in words]
    freq = {}

    for item in w:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return freq

print(word_counter("I am a girl"))

def letter_counter(text):
    words = text.split()
    w = [w.lower() for w in words]
    letters = []
    for word in w:
        for letter in word:
            letters.append(letter)

    freq = {}
    for item in letters:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return freq

print(letter_counter("I am a girl"))