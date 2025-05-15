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

print(random.randint(0, 10))
print(rock, paper, scissors)

# ASCII art from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
