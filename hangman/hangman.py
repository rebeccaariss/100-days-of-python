import random

#Step 1
# Word list from https://randomwordgenerator.com/
word_list = [ 'bubble', 'dilemma', 'grounds', 'revoke', 'condition', 'photocopy', 'notion', 'coalition', 'coincidence', 'constitutional', 'magazine', 'transparent', 'executive', 'bottom', 'housing', 'rotten', 'goalkeeper', 'colourful', 'invite', 'education', 'skilled', 'praise', 'visual', 'security', 'ignore', 'latest', 'oceanic', 'command', 'applied', 'document', 'launch', 'transaction', 'throat', 'tolerate', 'concentrate', 'emotion', 'invasion', 'throne', 'dilute', 'program', 'quantity', 'locate', 'guerrilla', 'species', 'course', 'promise', 'approve', 'school', 'mirror', 'conscience', ]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
placeholder = ''
for position in range(word_length):
  placeholder += '_'
# print(chosen_word)
print(placeholder)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input('Please guess a letter: ').lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# if guess in chosen_word:
#   print(chosen_word.index(guess))
#   index = chosen_word.index(guess)
#   # print(range(len(guess)))
# else:
#   print("No")

display = ''
for letter in chosen_word:
  display += '_'

while '_' in display:
  guess = input('Please guess a letter: ').lower()
  for letter in chosen_word:
    if letter == guess:
      display += letter
    else:
      display += '_'
  print(display)

# 
  #TODO-4 - Create a "placeholder" with the same number of blanks as the chosen_word
  #TODO-5 - Create a "display" that puts the guess letter in the right position