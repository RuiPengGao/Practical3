# Displaying matrix of 0s and 1s
import random

n = int(input("Enter an integer:"))
for i in range(n):
    for j in range(n):
        print(random.randint(0,1), end= ' ')
    print("\n")
