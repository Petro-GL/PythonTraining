# Create a random list of X elements, iterate through list of randoms and calculate its sum and average

#Creating a list of random numbers
from random import randint
randomlist = []
appendCounter = 0
while appendCounter < 10:
     randomInt = randint(0, 1000)
     randomlist.append(randomInt)
     appendCounter += 1
print("list of random numbers contains: " + str(randomlist) + "\n")

#Calculating summ
i = 0
summ = 0
print("Adding: ")
while i < len(randomlist):
    print(str(summ) + " + " + str(randomlist[i]))
    summ += randomlist[i]
    i += 1
print("Sum of all numbers: " + str(summ) + "\n")

#Calculating average
average = summ / len(randomlist)
print("Average number: " + str(average))