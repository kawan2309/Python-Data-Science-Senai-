import random



l = ['a','b','c']
n = [2,3,6,6,545]


d1  =  random.choice(l)
d2  =  random.choice(l)
d3  =  random.choice(l)
d4  =  random.choice(l)


d5  =  random.choice(n)
d6  =  random.choice(n)
d7  =  random.choice(n)
d8  =  random.choice(n)
lista = [d1,d5,d2,d6,d3,d7,d4,d8]


for n in lista:
    print(n, end= '')



