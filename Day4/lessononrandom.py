import random

randon_integer = random.randint(1, 100)

print(randon_integer)

randon_number = random.random()
print(randon_number)



random_float = random.uniform(1, 100)

if random_float > 50:
    print(f"The random number is {random_float}")
    print("Heads")
else:
    print(f"The random number is {random_float}")
    print("Tails")

