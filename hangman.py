import hangfuncs

# vars
win = False
mysteryWord = hangfuncs.GetWord()
wordArray = [i for i in mysteryWord]
mysteryArray = [" _ " for i in range(0, len(wordArray))]
wrongGuesses = []

#main loop
while(hangfuncs.lives > 0 and win == False):
  hangfuncs.os.system("clear")
  print("LIVES =  ", hangfuncs.lives, "   WRONG GUESSES: ", wrongGuesses)
  print("\n\n", mysteryArray)
  guess = hangfuncs.Guess()

  if mysteryWord.find(guess) != -1:
    for i in range(0, len(mysteryWord)):
      if(mysteryWord[i] == guess):
        mysteryArray[i] = guess
  elif guess not in wrongGuesses:
    hangfuncs.lives -= 1
    wrongGuesses.append(guess)

  if hangfuncs.lives == 0:
    print("YOU LOST, THE WORD WAS", mysteryWord.upper())

  if " _ " not in mysteryArray:
    win = True
    print("YOU WIN! THE WORD WAS", mysteryWord.upper())
