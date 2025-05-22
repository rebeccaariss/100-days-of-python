import random, time

# ASCII art from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

user_choice_images = {
    0: """
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """,
  1: """
      _______
  ---'    ____)___
            ______)
            _______)
          _______)
  ---.__________)
  """,
  2: """
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  """,
}

computer_choice_images = {
0: """
                                      _______
                                    _(____   '---
                                   (_____)
                                   (_____)
                                    (____)
                                     (___)__.---
""",
1: """
                                          _______
                                     ____(____    '---
                                    (______
                                   (_______
                                   (_______
                                     (__________.---
""",
2: """
                                          _______
                                     ____(____   '---
                                    (______
                                   (__________
                                        (____)
                                         (___)__.---
"""
}

outcome_messages = {
    (0, 0): "It's a draw.",
    (0, 1): "Paper covers rock. You lose.",
    (0, 2): "Rock smashes scissors. You win!",
    (1, 0): "Paper covers rock. You win!",
    (1, 1): "It's a draw.",
    (1, 2): "Scissors cut paper. You lose.",
    (2, 0): "Rock smashes scissors. You lose.",
    (2, 1): "Scissors cut paper. You win!",
    (2, 2): "It's a draw."
}

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:  "))
computer_choice = random.randint(0, 2)

# User choice == rock
if user_choice == 0 and computer_choice == 0:
  # TODO: Add you chose x, computer chose y, time delays, newlines \n, case for invalid number "you lose". ALTERNATIVE SOLUTION is to use 0, 1, 2. Refactor for that.
  print(user_choice_images[0], computer_choice_images[0], "It's a draw.")
elif user_choice == 0 and computer_choice == 1:
  print(user_choice_images[0], computer_choice_images[1], "Paper covers rock. You lose.")
elif user_choice == 0 and computer_choice == 2:
  print(user_choice_images[0], computer_choice_images[2], "Rock smashes scissors. You win!")

# User choice == paper
if user_choice == 1 and computer_choice == 0:
  print(user_choice_images[1], computer_choice_images[0], "Paper covers rock. You win!")
elif user_choice == 1 and computer_choice == 1:
  print(user_choice_images[1], computer_choice_images[1], "It's a draw.")
elif user_choice == 1 and computer_choice == 2:
  print(user_choice_images[1], computer_choice_images[2], "Scissors cut paper. You lose.")

# User choice == scissors
if user_choice == 2 and computer_choice == 0:
  print(user_choice_images[2], computer_choice_images[0], "Rock smashes scissors. You lose.")
elif user_choice == 2 and computer_choice == 1:
  print(user_choice_images[2], computer_choice_images[1], "Scissors cut paper. You win!")
elif user_choice == 2 and computer_choice == 2:
  print(user_choice_images[2], computer_choice_images[2], "It's a draw.")