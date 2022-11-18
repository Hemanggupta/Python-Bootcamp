def loveCalc(nameOne,nameTwo):
  t= nameOne.lower().count("t")  
  r= nameOne.lower().count("r")  
  u= nameOne.lower().count("u")  
  e= nameOne.lower().count("e")  
  true= t+r+u+e

  l= nameTwo.lower().count("l")
  o= nameTwo.lower().count("o")
  v= nameTwo.lower().count("v")
  e2= nameTwo.lower().count("e")
  love=l+o+v+e2

  percent = str(true) + str(love)
  print(f"Love percentage : {percent}%")

loveCalc("Angela Yu","Harbour Matham")