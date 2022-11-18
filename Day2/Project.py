print("Welcome to tip calculator.")
total = float(input('What was the total bill? $'))
percent = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input("How many people to split the bill? "))

totalTip = (percent/100*total) + total

perPerson=(totalTip/people)

# 2nd way to round floats
perPerson = "{:.2f}".format(perPerson)

print(f"Each person should pay: ${perPerson}")