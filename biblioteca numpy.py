import numpy as np
import timeit as tm

# array  com numpy
n = np.array([1,2,3])
print(n)

# arange()
r = np.arange(1,21)
print(r)

# matrizes: 

matriz = np.array([[1,2,3],[6,5,4],[5,6,7]])
print(matriz)

# valores aleatórios

matriz_al = np.random.rand(3,3)
print(matriz_al)


# soma  max min

soma  = np.sum(matriz_al)
minimo = np.min(matriz_al)
maximo  = np.max(matriz_al)
print(maximo) 


# media moda mediana

media  =  np.mean(matriz_al)
# moda  =  np.mod(matriz_al)
mediana  =  np.median(matriz_al)

print(media, mediana)

# matrizes de zero

arra_z = np.zeros(10)
print(arra_z)

# matriz com numeros 1

uns = np.ones([5])
print(uns)

# calculos aritméticos

a = np.array([1,2,3])
b = np.array([4,5,6])
somar =  a + b
print(somar)


# desvio  

ar =  np.array([1,2,3,4,5,6])
print(np.std(ar))

# slice


print(ar[:])

print(ar[0:3])


# mostrar subdivisões:

ar =  np.array([[1,2,3,4,5,6],[1,2,3],[123,45,89]])
n = ar[0,0]

