import modulo


lista =  [1.5,6.8,9.7,10.6]
lista.sort()
print(lista)
media_ = modulo.media(lista)
print('media', round(media_,2))


moda = modulo.moda(lista)
print('Moda:', moda)

med = modulo.mediana(lista)
print('Mediana', med)


# lista =  [1,2,3,4,5,6,6,2,2,2]
# print(lista)
# con = {1,2,3,5,6,6,2,2,2}
# print(con)


# if len(lista) == len(con):
#     print('Não tem')
# else:
#     print('Tem moda')
#     mode1  =  max(set(lista), key=lista.count)
#     print(mode1)

