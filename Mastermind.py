#Mastermind:
import random

colours = ["red", "blue", "pink", "grey", "green", "brown", "white", "black"]
complist = []
userlist = []

for i in range(1, 5):
    compchoice = random.choice(colours)
    complist.append(compchoice)

print(complist)

print(colours)
for i in range(1, 5):
    col = input("Please enter a colour. ")
    userlist.append(col)


print(userlist)


for i in range(len(complist)-1):
    for j in range(len(complist)-1):
        if complist[i] == userlist[j]:
            print("Great job!")
        else:
            print("YOu're dumb")