import random
a="Hemang,Gupta,Mohit,kapadia,Kritika,Dubey"
names= a.split(",")
# names= input("Enter the names:").split(",")


print(random.choice(names))
# print(names[random.randint(0, len(names)-1)])
