import random

def headtails():
  chance=random.randint(1,2)
  if(chance==1):
    chance="Heads"
  else:
    chance="Tails"
  return chance

print(headtails())