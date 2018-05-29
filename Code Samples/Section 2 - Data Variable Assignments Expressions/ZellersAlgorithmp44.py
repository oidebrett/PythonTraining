y = int(input("What are the last 2 digits of the year:"))
c = int(input("What are the first 2 digits of the year:"))
mm = int(input("What is the month:"))
dd = int(input("What is the day:"))

w = ((dd + ((13*(mm+1))/5)+y+(y/4)+(c/4)-2*c)%7)

print (w)


