import random
import os

def GetLives():
  return 7

def GetWord():
  words = (i.strip().lower() for i in open("wordlist.10000.txt", "r") if len(str(i)) > 4)
  randomWord = list(words)[random.randint(0, 8000)]
  return randomWord

def Guess():
  print("--- Guess a letter: \n")
  guess = input(">  ").lower()
  return guess

def GetEmptyList():
  emptyList = []
  return emptyList

def UpdateScore(score):
  file = open("score.txt", "w")
  file.write(str(score))
  file.close()

def GetScore():
  score = 0
  with open("score.txt", "r") as file:
    score = int(file.readline(1))

  return score