import random

comp_choice= random.randint(1,3)
# Cheating
print(comp_choice)

print("1 for Rock \n2 for Paper \n3 for Scissors")
choice=int(input("Enter a choice:"))

if choice>3:
  print("Invalid choice!")
elif choice == 1 and comp_choice==3:
  print("You Win!")
elif (choice > comp_choice):
  print("You Win!")
elif choice == comp_choice:
  print("Draw!")
else:
  print("You Lose!")