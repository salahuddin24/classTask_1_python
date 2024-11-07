
words = ["apple", "banana", "cherry", "blueberry", "kiwi"]


def print_word(x):
    find_index = words.index(x)
    print(find_index + 1,":", x)
    # return find_index + 1, ":", x
result = list(map(print_word, words))
# print(result)
