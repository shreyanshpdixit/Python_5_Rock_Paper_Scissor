rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

cpu = [rock, paper, scissors]
final = random.randint(0, 2)

choice = int(input())

if choice == 0:

    print(f"\nYou chose:\n{rock}")
    print("\nComputer chose:\n")
    print(cpu[final])
elif choice == 1:
    print(f"\nYou chose:\n{paper}")
    print("\nComputer chose:\n")
    print(cpu[final])
elif choice == 2:
    print(f"\nYou chose:\n{scissors}")
    print("\nComputer chose:\n")
    print(cpu[final])
else:
    print("Choose among 0,1 or 2 only.")


if choice == 0 and final == 0:
    print("\nIts a Draw...")
elif choice == 0 and final == 1:
    print("\nYou lose.")
elif choice == 0 and final == 2:
    print("\nYou won!")
elif choice == 1 and final == 0:
    print("\nYou won!")
elif choice == 1 and final == 1:
    print("\nIts a Draw...")
elif choice == 1 and final == 2:
    print("\nYou lose.")
elif choice == 2 and final == 0:
    print("\nYou lose.")
elif choice == 2 and final == 1:
    print("\nYou won!")
elif choice == 2 and final == 2:
    print("\nIts a Draw...")
else:
    print("Error")