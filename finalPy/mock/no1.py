def find_word_positions(word, list_of_words):
    word = word.lower()
    list_of_words = [w.lower() for w in list_of_words]
    result = []

    if word in list_of_words:
        for i in range(len(list_of_words)):
            if word == list_of_words[i]:
                result.append(i)

            else:
                pass
    else:
        result = 0
    return result

print(find_word_positions("Python", ["python", "java", "c", "PYTHON", "prolog"]))