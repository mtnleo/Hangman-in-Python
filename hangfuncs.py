import random
import os

lives = 7

def GetWord():
  words = (i.strip().lower() for i in open("wordlist.10000.txt", "r") if len(str(i)) > 4)
  randomWord = list(words)[random.randint(0, 10000)]
  return randomWord

def Guess():
  print("--- Guess a letter: \n")
  guess = input(">  ").lower()
  return guess


