import statisticsCriado as sts


empresa1 = [2500, 2800, 3000, 9500, 12000]
empresa1.sort()
empresa2 = [5000, 5200, 5300, 5400, 5500]
empresa2.sort()
empresa3 = [1000, 2000, 8000, 15000, 20000]
empresa3.sort()
empresa4 = [3500, 4000, 4200, 4300, 6000]
empresa4.sort()
empresa5 = [1200, 1500, 1800, 2500, 10000]
empresa5.sort()



#Verificando a média de valor que as empresas oferecem 
media_ = sts.media(empresa1)
print('Media 1', round(media_,2),'R$')

media_2 = sts.media(empresa2)
print('Media 2', round(media_2,2),'R$')

media_3 = sts.media(empresa3)
print('Media 3', round(media_3,2),'R$')

media_4 = sts.media(empresa4)
print('Media 4', round(media_4,2),'R$')

media_5 = sts.media(empresa5)
print('Media 5', round(media_5,2),'R$')

lista_empresa = ['tots','atl','tivit','santander','kwn']
calculo = [media_,media_2,media_3,media_4,media_5]
#soma    = sum(calculo)

media_mercado = sts.media(calculo)
print('Media paga pelo mercado é: ',media_mercado,'R$')
print ('')


# medi_m = [x for x in calculo if x >= media_mercado ]
# print(medi_m)

for media, empresa in zip(calculo, lista_empresa):
    if media > media_mercado:
        print(f'A {empresa} paga acima da média do mercado, valor pago pela empresa é: {round(media, 2)}R$')
        print ('Vale a pena $-$')
        print ('')



