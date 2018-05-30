import random

n1 = random.randint(0,12)
n2 = random.randint(0,12)
ans = n1 * n2

print("%d * %d" %(n1,n2))

foundCorrectAnswer = False

while not foundCorrectAnswer:
    usrAns = input("Enter your answer: ")
    if not usrAns.isdigit():
        print("You must enter a number")
        break
    else:
        usrAns = int(usrAns)

    if usrAns == ans:
        print("Correct")
        print("The correct answer was %d" %(n1*n2))

        foundCorrectAnswer = True
        usrContinue = input("Enter Y to continue or any other key to quit: ")
        usrContinue = usrContinue.upper()

        if usrContinue == 'Y':
            foundCorrectAnswer = False
            n1 = random.randint(0,12)
            n2 = random.randint(0,12)
            ans = n1 * n2
            print("%d * %d" %(n1,n2))
        else:
            print("Goodbye")
            break

            

    elif usrAns>ans:
        print("Too high")
    elif usrAns<ans:
        print("Too low")



