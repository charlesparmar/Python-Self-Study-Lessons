import time
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('''


Welcome to the CAP Password Generator!

READ THIS BEFORE YOU CONTINUE:
Password must be a combination of letters, symbols and numbers
Please enter the number of letters, symbols and numbers you would like to have in your password

Please make sure the number of letters is between 4 and 6

Please make sure the number of symbols is between 2 and 4

Please make sure the number of numbers is between 2 and 4

Password must be at least 8 characters long and at most 16 characters long''')


print("Please hit enter to continue...")
input()

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

if nr_letters < 4 or nr_letters > 6:
    print("The number of letters is not between 4 and 6. Please try again.")
    exit()
if nr_symbols < 2 or nr_symbols > 4:
    print("The number of symbols is not between 2 and 4. Please try again.")
    exit()
if nr_numbers < 2 or nr_numbers > 4:
    print("The number of numbers is not between 2 and 4. Please try again.")
    exit()

print('''

Thinking which letters to take...''')
time.sleep(1)
print('''

Thinking which symbols to take...''')
time.sleep(1)
print('''

Thinking which numbers to take...''')
time.sleep(1)
print('''

Generating password...

''')
time.sleep(2)

password = []



for i in range(1, nr_letters + 1):
    clet = random.choice(letters)
    password.append(clet)

for i in range(1, nr_symbols + 1):
    clet = random.choice(symbols)
    password += clet

for i in range(1, nr_numbers + 1):
    password += random.choice(numbers)
    # clet = random.choice(numbers)
    # password.append(clet)

random.shuffle(password)
# print(password)


p_password = ""
for let in password:
    p_password += f"{let}"


print(f'''The random password you could use is '{p_password}'. Please note that this password is case sensitive

Thank you for using the PyPassword Generator!

''')
