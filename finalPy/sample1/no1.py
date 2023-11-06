##Write a Python function count_occurrences(word, list_of_words) to count how many times the string word occurs in the list list_of_words. 
##The function should be case-insensitive.

def count_occurrences(word, list_of_words):
    word = word.lower()
    list_of_words = [w.lower() for w in list_of_words]
    count = 0
    for i in range(len(list_of_words)):
        if word == list_of_words[i]:
            count += 1
        else:
            pass

    return count

word_list = ["python", "Python", "C", "c++"]
print(count_occurrences("python", word_list))