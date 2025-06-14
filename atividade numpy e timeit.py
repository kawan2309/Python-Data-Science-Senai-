import numpy as np
import timeit as tm

#1. Crie um array de 20 elementos.
r = np.arange(1,21)
print(r)

#2. Extraia os primeiros 5 elementos, os últimos 5 elementos e os elementos das posições 5 a 10.
r = np.arange(1,12)
array = np.array(r)
print(array)
posi_elemento1 = array[5:10]
# posi_elemento2 = array[9]

primeiros_cinco = array[:5]
ultimos_cinco = array[-5:]

print('Primeiros cinco: ',primeiros_cinco)
print('Ultimos cinco: ',ultimos_cinco)
print('Numero da posição:', posi_elemento1)
# print('Numero da posição 10:', posi_elemento2)

