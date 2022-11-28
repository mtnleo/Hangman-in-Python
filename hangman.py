import random
import os

lives = 7

def GetWord():
  words = (i.strip().lower() for i in open("wordlist.10000.txt", "r"))
  randomWord = list(words)[random.randint(0, 10000)]
  return randomWord

def Guess():
  print("--- Guess a letter: \n")
  guess = input(">  ").lower()
  return guess


mysteryWord = GetWord()
wordArray = [i for i in mysteryWord]
mysteryArray = [" _ " for i in range(0, len(wordArray))]
wrongGuesses = []

win = False

while(lives > 0 and win == False):
  os.system("clear")
  print("LIVES =  ", lives, "   WRONG GUESSES: ", wrongGuesses)
  print("\n\n", mysteryArray)
  guess = Guess()

  if mysteryWord.find(guess) != -1:
    for i in range(0, len(mysteryWord)):
      if(mysteryWord[i] == guess):
        mysteryArray[i] = guess
  elif guess not in wrongGuesses:
    lives -= 1
    wrongGuesses.append(guess)

  if lives == 0:
    print("YOU LOST, THE WORD WAS", mysteryWord.upper())

  if " _ " not in mysteryArray:
    win = True
    print("YOU WIN! THE WORD WAS", mysteryWord.upper())
