# Write a Python function is_anagram(word1, word2) that checks if two words are anagrams of each other. The function should return True if they are anagrams and False otherwise. The comparison should be case-insensitive.

def is_anagram(word1, word2):
    # Convert both words to lowercase for case-insensitive comparison
    word1 = word1.lower()
    word2 = word2.lower()

    # Initialize dictionaries to store character frequencies
    freq1 = {}
    freq2 = {}

    # Populate freq1 with character frequencies from word1
    for char in word1:
        if char.isalpha():
            if char in freq1:
                freq1[char] += 1
            else:
                freq1[char] = 1

    # Populate freq2 with character frequencies from word2
    for char in word2:
        if char.isalpha():
            if char in freq2:
                freq2[char] += 1
            else:
                freq2[char] = 1

    # Compare the frequencies of characters
    if len(freq1) != len(freq2):
        return False
    
    for char, count in freq1.items():
        if char not in freq2 or freq2[char] != count:
            return False
    
    return True

word1 = "listen"
word2 = "silent"
print(is_anagram(word1, word2))

def is_word_anagram(word):
    # Define a list of words to check against
    words_to_check = ["listen", "silent", "word", "drow"]

    # Check if the word is an anagram of any word in the list
    for w in words_to_check:
        if is_anagram(word, w):
            return True
    
    return False

word = "listen"
print(is_word_anagram(word))

# Define a function to match lists
def isAnagram(str1, str2):
    # Declare two empty lists
    l1 = []
    l2 = []

    # Convert first string into lowercase, append to list 1
    for i in str1:
        l1.append(i.lower())

    # Implement Bubble Sort for list 1
    n1 = len(l1)
    for i in range(n1):
        for j in range(0, n1-i-1):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]

    # Convert second string into lowercase, append to list 2
    for j in str2:
        l2.append(j.lower())

    # Implement Bubble Sort for list 2
    n2 = len(l2)
    for i in range(n2):
        for j in range(0, n2-i-1):
            if l2[j] > l2[j+1]:
                l2[j], l2[j+1] = l2[j+1], l2[j]

    if l1 == l2:
        return "The strings are anagrams."
    else:
        return "The strings are not anagrams."

result = isAnagram("listen", "silent")
print(result)
