import random

#Step 1
# Word list from https://randomwordgenerator.com/
word_list = [ "bubble", "dilemma", "grounds", "revoke", "condition", "photocopy", "notion", "coalition", "coincidence", "constitutional", "magazine", "transparent", "executive", "bottom", "housing", "rotten", "goalkeeper", "colourful", "invite", "education", "skilled", "praise", "visual", "security", "ignore", "latest", "oceanic", "command", "applied", "document", "launch", "transaction", "throat", "tolerate", "concentrate", "emotion", "invasion", "throne", "dilute", "program", "quantity", "locate", "guerrilla", "species", "course", "promise", "approve", "school", "mirror", "conscience", ]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
