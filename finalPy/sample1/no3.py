# Write a Python function remove_duplicates(list_of_words) that removes duplicates from a list of words.
# The function should return a new list without any duplicates.

def remove_duplicates(list_of_words):
    new_list = []
    for word in list_of_words:
        if word not in new_list:
            new_list.append(word)

    return new_list

#case insensitive
def remove_dupes_case(list_of_words):
    new_list = []
    list_of_words = [w.lower() for w in list_of_words]

    for word in list_of_words:
        if word not in new_list:
            new_list.append(word)

    return new_list

list = ["python", "Python", "c", "C", "adng", "dkv"]

print(remove_duplicates(list))
print(remove_dupes_case(list))