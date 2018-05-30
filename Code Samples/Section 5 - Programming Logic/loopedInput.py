# using a for loop to get input and keep a runningTotal

runningTotal = 0

for i in range(5):
    runningTotal = runningTotal + int(input("Enter a number: "))

print("Total is %d" %(runningTotal))


# using a while loop to get input and keep a runningTotal

runningTotal = 0
i=0

while i<5:
    runningTotal = runningTotal + int(input("Enter a number: "))
    i=i+1

print("Total is %d" %(runningTotal))

# using a while loop to get input and keep a runningTotal
# keep going until value entered is not zero

runningTotal = 0
done = False
i=0

while not done:
    enteredNumber = int(input("Enter a number: "))
    if enteredNumber == 0:
        done = True
    runningTotal = runningTotal + enteredNumber
    i=i+1

print("Total is %d" %(runningTotal))

# using a while loop to get input and keep a runningTotal
# keep going until value entered is not zero
# version 2

runningTotal = 0
i=0

enteredNumber = int(input("Enter a number: "))
while enteredNumber!=0:
    runningTotal = runningTotal + enteredNumber
    enteredNumber = int(input("Enter a number: "))
    i=i+1

print("Total is %d" %(runningTotal))