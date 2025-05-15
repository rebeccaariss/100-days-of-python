import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_reversed = """
                                      _______
                                    _(____   '---
                                   (_____)
                                   (_____)
                                    (____)
                                     (___)__.---
"""

paper_reversed = """
                                          _______
                                     ____(____    '---
                                    (______
                                   (_______
                                   (_______
                                     (__________.---
"""

scissors_reversed = """
                                          _______
                                     ____(____   '---
                                    (______
                                   (__________
                                        (____)
                                         (___)__.---
"""

# print(random.randint(0, 10))
# print(rock, paper, scissors)

# ASCII art from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:  "))
computer_choice = random.randint(0, 2)

# if user_choice == 0:
#   print(rock, rock_reversed)
# elif user_choice == 1:
#   print(paper, paper_reversed)
# elif user_choice == 2:
#   print(scissors, scissors_reversed)

# User choice == rock
if user_choice == 0 and computer_choice == 0:
  print(rock, rock_reversed, "It's a draw.")
elif user_choice == 0 and computer_choice == 1:
  print(rock, paper_reversed, "Paper covers rock. You lose.")
elif user_choice == 0 and computer_choice == 2:
  print(rock, scissors_reversed, "Rock smashes scissors. You win!")
scissors

# User choice == paper
if user_choice == 1 and computer_choice == 0:
  print(paper, rock_reversed, "Paper covers rock. You win!")
elif user_choice == 1 and computer_choice == 1:
  print(paper, paper_reversed, "It's a draw.")
elif user_choice == 1 and computer_choice == 2:
  print(paper, scissors_reversed, "Scissors cut paper. You lose.")

# User choice == scissors
if user_choice == 2 and computer_choice == 0:
  print(scissors, rock_reversed, "Rock smashes scissors. You lose.")
elif user_choice == 2 and computer_choice == 1:
  print(scissors, paper_reversed, "Scissors cut paper. You win!")
elif user_choice == 2 and computer_choice == 2:
  print(scissors, scissors_reversed, "It's a draw.")