principal=input("Enter Principal: ")
principal=float(principal)

rate=input("Enter rate:")
rate=float(rate)

time=input("Enter time in years:")
time=float(time)
amount = principal*rate*time

print("The interest amount is: ", amount)