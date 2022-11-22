alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo

def ceasar_cipher():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  # ENCRYPTING
  if direction=="encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encripted_code=""
    for i in text:
      if i.isalpha():
        encripted_code+=alphabet[(alphabet.index(i)+shift)%26]
      else:
        encripted_code+=i
    return encripted_code
  # DECRYPTING
  elif direction=="decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    plain_text=""
    for i in text:
      if i.isalpha():
        plain_text+=alphabet[(alphabet.index(i) - shift)%26]
        # %26 is not needed.. alphabet[-1]==z
      else: 
        plain_text+=i
    return plain_text  
  else:
    return "Wrong Choice!"
  
print(logo)

try_again=True
while try_again:
  print(ceasar_cipher())
  run_again= input("Enter 'Y' to run again and 'N' to end: ").lower()
  if run_again=="n":
    try_again=False
    print("<--END-->")
