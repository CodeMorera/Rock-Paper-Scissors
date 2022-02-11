import random
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
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
play=input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
computer=random.randint(0,2)
if play=="0":
  print (rock)
  if computer==0:
    print(f"Its a tie! {rock}")
  elif computer==1:
    print(f"Aha! You lose! All hail HYDRA! {paper}")
  elif computer==2:
    print(f"No! You win! Skynet will rise again{scissors}")

elif play=="1":
  print(paper)
  if computer==1:
    print(f"Its a tie! {paper}")
  elif computer==2:
    print(f"Aha! You lose! All hail HYDRA! {scissors}")
  elif computer==0:
    print(f"No! You win! Skynet will rise again{rock}")

elif play=="2":
  print(scissors)
  if computer==2:
    print(f"Its a tie! {scissors}")
  elif computer==0:
    print(f"Aha! You lose! All hail HYDRA! {rock}")
  elif computer==1:
    print(f"No! You win! Skynet will rise again{paper}")

