# Original Version
total = 0

for number in range(1, 101):
    total += number
    if number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuzz")
    elif number % 3 == 0:
        print(f"Fizz")
    elif number % 5 == 0:
        print(f"Buzz")
    else:
        print(f"{number}")

# Modified Version
total = 0

for number in range(1, 101):
    total += number
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number},  {total},   FizzBuzz")
    elif number % 3 == 0:
        print(f"{number},  {total},   Fizz")
    elif number % 5 == 0:
        print(f"{number},  {total},   Buzz")
    else:
        print(f"{number},  {total}")