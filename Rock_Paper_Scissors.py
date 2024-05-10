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

#Write your code below this line 👇
import random

choice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if choice=="0":
  print(rock)
elif choice=="1":
  print(paper)
elif choice=="2":
  print(scissors)
else:
    print("Invalid Choice.")

computer=random.randint(0,2)
if computer==0:
    print(rock)
elif computer==1:
    print(paper)
elif computer==2:
    print(scissors)

if choice=="0" and computer==0:
    print("Its a draw.\nXD")
elif choice=="1" and computer==0:
    print("You win.\n:)")
elif choice=="2" and computer==0:
    print("You lose. \n:(")
elif choice=="0" and computer==1:
    print("You lose. \n:(")
elif choice=="1" and computer==1:
    print("Its a draw.\nXD")
elif choice=="2" and computer==1:
    print("You win.\n:)")
elif choice=="0" and computer==2:
    print("You win.\n:)")
elif choice=="1" and computer==2:
    print("You lose. \n:(")
elif choice=="2" and computer==2:
    print("Its a draw.\nXD")
