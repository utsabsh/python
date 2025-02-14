import random

# Define character pools
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&()*+"

print("Welcome to the PyPassword Generator!")

# Get user input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generate password parts
password_easy = (
    "".join(random.choices(letters, k=nr_letters)) +
    "".join(random.choices(symbols, k=nr_symbols)) +
    "".join(random.choices(numbers, k=nr_numbers))
)
print(f"Easy Password (Ordered): {password_easy}")

# Hard Level - Randomized order
password_list = (
    random.choices(letters, k=nr_letters) +
    random.choices(symbols, k=nr_symbols) +
    random.choices(numbers, k=nr_numbers)
)
random.shuffle(password_list)
password_hard = "".join(password_list)

print(f"Hard Password (Shuffled): {password_hard}")
S