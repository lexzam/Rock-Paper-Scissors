import random
import art

def game():
  choise = int(input("\nWhat do you choose? Rock(0), Paper(1) or Scissors(2).\n").lower())
  
  if choise == 0:
    print(art.rock)
  elif choise == 1:
    print(art.paper)
  elif choise == 2:
    print(art.scissors)
  else:
    print("Wrong input")
  
  print("\nComputer chose:")
  
  rock_paper_scissors = random.randint(0,2)
  
  if rock_paper_scissors == 0:
    print(art.rock)
  elif rock_paper_scissors == 1:
    print(art.paper)
  else:
    print(art.scissors)
  
  if choise == 0 and rock_paper_scissors == 2:
    print("You win!!")
  elif choise == 2 and rock_paper_scissors == 0:
    print("You lose.")
  elif choise == rock_paper_scissors:
    print("It's a draw.")
  elif choise >= 3 or choise < 0:
    print("Invalid.")
  elif choise < rock_paper_scissors:
    print("You lose.")
  elif choise > rock_paper_scissors:
    print("You win!!")
  return
game()
while True:
  repent=input("\nDo you want to play again? 'y' or 'n' ")
  if repent == 'y':
    game()
  else:
    break
