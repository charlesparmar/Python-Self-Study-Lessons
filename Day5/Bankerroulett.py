import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

position = random.randint(0, len(friends)-1)

print(random.choice(friends))

print(f"The lucky winner is {friends[position]}")