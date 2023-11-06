#merging dictionaries

dict1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

dict2 = {
    'c': 4,
    'd': 5,
    'e': 6
}

def merge(dict1, dict2):
    merged_dict = {}
    for key, value in dict1.items():
        merged_dict[key] = value

    for key1, value1 in dict2.items():
        if key1 in merged_dict:
            merged_dict[key1] = value1

        else: 
            merged_dict[key1] = value1

    return merged_dict

print(merge(dict1, dict2))

def inverse(dict1):
    inversed = {}
    for key, value in dict1.items():
        inversed[value] = key

    return inversed

print(inverse(dict1))