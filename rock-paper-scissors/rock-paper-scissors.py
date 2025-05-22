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

try:
  time.sleep(0.25)
  user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:  "))
  if user_choice not in [0, 1, 2]:
    raise ValueError("Invalid number")
  
  computer_choice = random.randint(0, 2)

  print("\nYou chose:\n")
  print(user_choice_images[user_choice])
  time.sleep(1.5)
  print("                                        Computer chose:\n")
  print(computer_choice_images[computer_choice])
  time.sleep(1.5)

  print("\n" + outcome_messages[(user_choice, computer_choice)])


except ValueError:
  print("Invalid input. Please try again.")