# In Python, both stack and queue are abstract data structures that store elements but differ in how they allow you to access, insert, and remove elements.
# stack example
books = []
books.append("learn C")
books.append("learn C++")
books.append("learn python")
books.append("learn javaScript")
books.append("learn java")
print(books)
books.pop() # sesher dik theke akta item bad dibe
print("now the top book is : ", books[-1])
books.pop()
print("now the top book is : ", books[-1])

books.pop()
if not books:
    print("No books left")

# queue
from collections import  deque
bank = deque(["Anis", "Karim", "Bijoy"])
print(bank)
bank.popleft() # left/shuru theke 1 ta value bad dibe
print(bank)
bank.popleft()
bank.popleft()
print(bank)

if not bank:
    print("No person left")








