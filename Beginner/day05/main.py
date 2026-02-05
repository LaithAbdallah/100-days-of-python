import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total = [nr_letters, nr_symbols, nr_numbers]
password_length = nr_letters + nr_symbols + nr_numbers
password = ""

# Easy Version, letters -> symbols -> numbers
for count in range (password_length):
    if nr_letters:
        password += random.choice(letters)
        nr_letters -= 1
    elif nr_symbols:
        password += random.choice(symbols)
        nr_symbols -= 1
    elif nr_numbers:
        password += random.choice(numbers)
        nr_numbers -= 1
print(f"Easy Password: {password}")

# Hard Version, random order
password = ""
random_int = 0
for count in range(password_length):
    random_int = random.randint(0, 2)
    while not total[random_int]:
        random_int = random.randint(0,2)
    if random_int == 0:
        password += random.choice(letters)
    elif random_int == 1:
        password += random.choice(symbols)
    else:
        password += random.choice(numbers)
    total[random_int] -= 1
print(f"Hard Password: {password}")
