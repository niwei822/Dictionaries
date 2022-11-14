"""Count words in file."""
import sys

# put your code here.
fish_locations = {"shark": "ocean", "salmon": "river"}
#print("salmon" in fish_locations)

#dict.get() 
scores = {"Bob": 10, "Joe": 3, "Jack": 6, "Jane": 15}
#print(scores.get("Jack"))
#if key not in the dict, return None
#print(scores.get("abc"))
#pass in additional argument, it will return a fallback value.
# print(scores.get("abc", 5))
# print(scores)

#dict.items()
#Return a new view of the dictionary’s items ((key, value) pairs).
#view is unordered but can loop over and return tuples(key, value)
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict.items())
# for item in my_dict.items():
#     print(f"key = {item[0]}, value = {item[1]}")
#print(sys.argv)


def tokenize(filename):
    token = []
    with open(filename) as data:
        for line in data:
            word = line.rstrip().split(" ")
            token.extend(word)
    return token
#tokenize("test.txt")
     
def count_words(words):
    words_counts = {}
    for word in words:
        words_counts[word] = words_counts.get(word, 0) + 1
    return words_counts
#count_words(["apple", "berry", "cherry", "apple"])

def print_word_counts(word_counts):
    for word, count in word_counts.items():
      print(word, count)
        
filename = "test.txt"
token = tokenize(filename)
words_counts = count_words(token)
print_word_counts(words_counts)
       