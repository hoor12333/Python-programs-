import random

# Random integer between 1 and 10
print("Random integer (1-10):", random.randint(1, 10))

# Random float between 0 and 1
print("Random float:", random.random())

# Random choice from a list
fruits = ["apple", "banana", "cherry", "mango"]
print("Random fruit:", random.choice(fruits))

# Shuffle a list
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print("Shuffled cards:", cards)
