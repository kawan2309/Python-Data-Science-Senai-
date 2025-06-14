#média, moda, mediana e desvio padrão, amplitude, variância


import statistics as sts


#lista  =  [100,99,100,98,100,99,111,100]
#lista.sort() # .sort() é igual order by, o padrão é sempre do menor pro maior



def media(lista):
    media1 =  sts.mean(lista)
    return media1


def moda(lista):
    moda1 =  sts.mode(lista)
    return moda1


def mediana(lista):
    mediana1 =  sts.median(lista)
    return mediana1

def amplitude(lista):
    amplitude_ =  max(lista) -  min(lista)
    return amplitude_


def variancia(lista):
    varian =  sts.variance(lista)
    return varian


def desvio(lista):
    des_padrao =  sts.stdev(lista)
    return des_padrao


