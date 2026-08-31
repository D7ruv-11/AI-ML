words = ["apple", "banana", "kiwi", "cherry", "mango"]
fruits = {}

for w in words:
    fruits.update({w: len(w)})

print(fruits)