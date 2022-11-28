import random

arr = ("Rock", "Paper", "Scissors")

cont = 'y'
userPick = 0
aiPick = 0

while cont == 'y':
  print("----- Welcome to rock, paper, scissors -----\nSelect one option:")
  userPick = int(input("     1. Rock   | 2. Paper   | 3. Scissors\n"))
  aiPick = random.randint(1, 3)

  print("AI Pick: ", arr[aiPick-1])
  
  if userPick == aiPick:
    print("It's a draw!")
  else:
    if userPick == 1:
      if aiPick == 2:
        print("You lost!")
      else:
        print("You won!")
    elif userPick == 2:
      if aiPick == 3:
        print("You lost!")
      else:
        print("You won!")
    elif userPick == 3:
      if aiPick == 1:
        print("You lost!")
      else:
        print("You won!")
    else:
      print("Pick a valid number")

    
  cont = input("\n----- Do you want to keep playing? ('y/n') ------\n")
    
  