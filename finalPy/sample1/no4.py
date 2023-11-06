# Implement a Python function find_common_words(list1, list2) that takes two lists of words and returns a list of words that are common between the two lists.
# The function should be case-insensitive.

def find_common_words(list1, list2):
    list1 = [w.lower() for w in list1]
    list2 = [w.lower() for w in list2]

    new_list= []
    for word in list1:
        if word in list2:
            new_list.append(word)

    return new_list

list1 = ["a", "b", "c", "d", "e"]
list2 = ["b", "c", "f", "e"]

print(find_common_words(list1, list2))