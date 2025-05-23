import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

number_of_letters = int(input('How many letters would you like in your password? '))
number_of_numbers = int(input('How many numbers would you like in your password? '))
number_of_symbols = int(input('How many symbols would you like in your password? '))

print(letters, numbers, symbols)

# Level 1:
sequential_pwd = ''
for x in range(number_of_letters):
  # sequential_pwd += letters[random.randint(0, 51)]
  sequential_pwd += random.choice(letters)

print(f"Your password is {sequential_pwd}")

# Level 2:
shuffled_pwd = ''