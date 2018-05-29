import random

article =['the','a','one','some','any']
noun =['boy','girl','dog','town','car']
verb =['drove','jumped','ran','walked','skipped']
preposition =['to','from','over','under','on']
noun2 = ['moon','school','home','town','heaven']

sentence = ""

r = random.randint(0,4)
word = article[r]
sentence = sentence + word + " "

r = random.randint(0,4)
word = noun[r]
sentence = sentence + word + " "

r = random.randint(0,4)
word = verb[r]
sentence = sentence + word + " "

r = random.randint(0,4)
word = preposition[r]
sentence = sentence + word + " "

r = random.randint(0,4)
word = noun2[r]
sentence = sentence + word + " "

print(sentence)