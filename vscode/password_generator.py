import random

# Define the character set to choose from
chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]|;:",.<>?/~`'

# Get the desired password length from the user
length = int(input("Enter the length: "))

# Generate the password using a list comprehension
password = ''.join(random.choice(chars) for _ in range(length))

# Print the final generated password
print("Password:- ",password)
