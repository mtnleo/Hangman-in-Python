import hangfuncs

#main loop
cont = 'y'

while cont == 'y':
  
  # vars
  score = hangfuncs.GetScore()
  lives = hangfuncs.GetLives()
  win = False
  mysteryWord = hangfuncs.GetWord()
  wordArray = [i for i in mysteryWord]
  mysteryArray = [" _ " for i in range(0, len(wordArray))]
  wrongGuesses = hangfuncs.GetEmptyList()

  # main game
  while (lives > 0 and win == False):
    hangfuncs.os.system("clear")
    print("LIVES =  ", lives, "         WRONG GUESSES: ", wrongGuesses, "\n\nSCORE =  ", score)
    print("\n\n", mysteryArray)
    guess = hangfuncs.Guess()
  
    if mysteryWord.find(guess) != -1:
      for i in range(0, len(mysteryWord)):
        if (mysteryWord[i] == guess):
          mysteryArray[i] = guess
    elif guess not in wrongGuesses:
      lives -= 1
      wrongGuesses.append(guess)
  
    if lives == 0:
      print("YOU LOST, THE WORD WAS", mysteryWord.upper())
  
    if " _ " not in mysteryArray:
      win = True
      print("YOU WIN! THE WORD WAS", mysteryWord.upper())
      score += 1
      hangfuncs.UpdateScore(score)
      

  cont = input("Do you want to play again? ('y/n')\n")
