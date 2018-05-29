#Caesar Cipher
inStr = input("Enter any character: ")
outStr = chr(ord(inStr)+1)
print(outStr)

inStr = input("Enter a 6 letter string: ")
outStr = ""
outStr = outStr + chr(ord(inStr[0])+1)
outStr = outStr + chr(ord(inStr[1])+1)
outStr = outStr + chr(ord(inStr[2])+1)
outStr = outStr + chr(ord(inStr[3])+1)
outStr = outStr + chr(ord(inStr[4])+1)
outStr = outStr + chr(ord(inStr[5])+1)
print(outStr)
