
def words_lengths(word_list):
    return [len(word) for word in word_list]

# Example usage
words = ["apple", "banana", "cherry", "blueberry", "kiwi"]
lengths = words_lengths(words)

# Print the result
print("Words:", words)
print("Lengths:", lengths)