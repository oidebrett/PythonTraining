import random

article =['the','a','one','some','any']
noun =['boy','girl','dog','town','car']
verb =['drove','jumped','ran','walked','skipped']
preposition =['to','from','over','under','on']

r = random.randint(0,4)
word = article[r]
r = random.randint(0,4)
word = noun[r]
r = random.randint(0,4)
word = verb[r]
r = random.randint(0,4)
word = preposition[r]

print(word)