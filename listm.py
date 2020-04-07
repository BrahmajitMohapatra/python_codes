import random
a = random.sample(range(15), 13)
print(a)
b= random.sample(range(10),8)
print(b)
c=[j for j in a if j in b]
print(c)
