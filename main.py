import statisticsCriado as stc


lista =  [1,2,4,5,360]
lista.sort()
print(lista)
media_ = stc.media(lista)
print('media', media_)


moda = stc.moda(lista)
print('Moda:', moda)

med = stc.mediana(lista)
print('Mediana', med)




