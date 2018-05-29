import random

mark = random.randint(0,100)

print("mark is %d " %mark)

if mark>=90:
    print("H0")
elif mark>=80:
    print("H2")
elif mark>=70:
    print("H3")
elif mark>=60:
    print("H4")
elif mark>=50:
    print("H5")
elif mark>=40:
    print("H6")
elif mark>=30:
    print("H7")
else:
    print("H8")

print("Well done!")
