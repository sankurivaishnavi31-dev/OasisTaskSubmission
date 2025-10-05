import random
import string

# Step 1: Get user input
length = int(input("Enter the desired password length: "))

include_letters = input("Include letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Step 2: Create character pool
characters = ""
if include_letters:
    characters += string.ascii_letters  # A-Z, a-z
if include_numbers:
    characters += string.digits         # 0-9
if include_symbols:
    characters += string.punctuation    # !@#$%^&*()

# Step 3: Generate password
if characters == "":
    print("You must select at least one character type!")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nYour generated password is: {password}")
