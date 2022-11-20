import random

def passGen():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  numbers = ['0','1','2','3','4','5','6','7','8','9']
  symbols = ['!','@','#','%','&','(',')','*','+','-']

  print("Welcome to the PyPassword Generator!")
  nr_letters = int(input("How many letters would you like in your password? "))
  nr_symbols = int(input("How many characters would you like? "))
  nr_numbers = int(input("How many numbers would you like? "))
  password = ""
  
  for i in range(0,nr_letters):
    password+=random.choice(letters)
  for j in range(0,nr_symbols):
    password+=random.choice(symbols)
  for k in range(0,nr_numbers):
    password+=random.choice(numbers)
  return password
  
print(passGen())