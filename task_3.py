# user_input = input("Enter a list of words separated by spaces:")
# word_list = user_input.split()
# print(word_list)
# n = input("Enter a number :")

word_list = ('apple', 'orange', 'pinaple', 'jekfruits', 'mango', 'amm')
n = 5
def filter_long_words(words, n):
    final_list = list(filter(lambda word: len(word) >n, word_list))
    print(final_list)



filter_long_words(word_list, 5)





