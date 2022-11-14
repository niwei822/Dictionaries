"""Count words in file."""


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

data = open("twain.txt")
word_counts = {}
for line in data:
    words = line.rstrip().split(" ")
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
for item in word_counts.items():
    print(item[0], item[1])
        
    
    