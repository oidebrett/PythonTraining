#this program usings a list to store the number of times a number is rolled on a dice
import random

counts = [0,0,0,0,0,0] # stores the counts for each number i.e. counts[0] stores count for the number 1

for count in range(50):
    r = random.randint(1,6)
    if r==1: counts[0] = counts[0] +1
    elif r==2: counts[1] = counts[1] +1
    elif r==3: counts[2] = counts[2] +1
    elif r==4: counts[3] = counts[3] +1
    elif r==5: counts[4] = counts[4] +1
    elif r==6: counts[5] = counts[5] +1

print(counts)

#even better way

counts = [0,0,0,0,0,0] # stores the counts for each number i.e. counts[0] stores count for the number 1

for count in range(50):
    r = random.randint(1,6)
    counts[r-1]=counts[r-1]+1


print(counts)