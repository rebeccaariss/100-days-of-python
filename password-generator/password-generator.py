import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

num_letters = int(input('How many letters would you like in your password? '))
num_numbers = int(input('How many numbers would you like in your password? '))
num_symbols = int(input('How many symbols would you like in your password? '))

# Level 1:
sequential_pwd = ''
for x in range(num_letters):
  sequential_pwd += random.choice(letters)
for x in range(num_numbers):
  sequential_pwd += random.choice(numbers)
for x in range(num_symbols):
  sequential_pwd += random.choice(symbols)

print(f"Your password is {sequential_pwd}")

# Level 2:
shuffled_pwd = ''