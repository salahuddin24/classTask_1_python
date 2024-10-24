user_input = input("Enter a list of words separated by spaces:")
word_list = user_input.split()
print(word_list)

# word_list = ('apple', 'orange', 'pinaple', 'jekfruits', 'mango', 'amm')

def find_longest_word(words) :
    longest_word = max(words, key=len)
    # print(longest_word)
    return len(longest_word)


lenght = find_longest_word(word_list)
print(lenght)


