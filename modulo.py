import statisticsCriado as sts


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
