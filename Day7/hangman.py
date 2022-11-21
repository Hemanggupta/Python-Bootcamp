import random
import words
import hangman_art
from replit import clear
#Step 1 

word_of_the_game= random.choice(words.word_list).lower()
total_chance=6
word_to_display= ["_"]*len(word_of_the_game)
print(hangman_art.logo)
while(total_chance>0):
  count = 0
  word=""
  print("")
  for i in word_to_display:
    print(i,end=" ")
    
  print(hangman_art.stages[total_chance])
# INPUT
  choice= input("Enter a letter: ").lower()
  
# CHECKING
  for i in range(len(word_of_the_game)):
    if(word_of_the_game[i]==choice):
      word_to_display[i]=choice
      count+=1
  if(count==0):
    total_chance-=1
  if(total_chance==0):
    print(hangman_art.stages[total_chance])
    print("You Lost!")
    print(f"The word was: {word_of_the_game}\n")
  if "_" not in word_to_display:
    print("\nYou Win!")
    print(f"The word was: {word_of_the_game}\n")
    total_chance=0
  