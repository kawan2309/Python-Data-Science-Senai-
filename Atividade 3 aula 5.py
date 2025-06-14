
import random
def calcula_media(n1,n2,n3,n4):
    
    calculo = [n1,n2,n3,n4]
    media   = sum(calculo)/len(calculo)
    return media

def medias():

    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    nota3 = float(input('nota 3: '))
    nota4 = float(input('nota 4: '))

    calcula_media_total = calcula_media(nota1,nota2,nota3,nota4)
    #print('media é: ',round(calcula_media_total,2))
    return calcula_media_total

def alunos():
    lista_alunos = ['Kaleb','Kaio','Kawan']
    
    media_1 = medias()
    media_2 = medias()
    media_3 = medias()


    print(f'''
           Media - {lista_alunos[0]} é {media_1}
           Media - {lista_alunos[1]} é {media_2}
           Media - {lista_alunos[2]} é {media_3}
          ''')
    
alunos()

# def IMC():
#     Peso   = float(input('Digite seu Peso: '))
#     Altura = float(input('Digite sua Altura exe: 1.75 '))
    
    
#     Altura_quadrado = Altura*Altura
#     calculo = round(Peso,2)/round(Altura_quadrado,2)
    
#     print('Valor: ',round(calculo,2))

#     if calculo < 18.5:
#        print('Peso inferior ao normal')
#     elif calculo >= 18.5 and calculo <= 24.9:
#        print('Peso normal')
#     elif calculo >= 25.0 and calculo <= 29.9:
#        print('Sobre peso')
#     elif calculo >= 30.0 and calculo <= 34.9:
#        print('Obesidade grau 1')
#     elif calculo >= 35.0 and calculo <= 39.9:
#            print('Obesidade grau 2')
#     elif calculo >= 40.0:
#         print('Obesidade grau 3')

# IMC()

def loop():            
    while True: 
        alunos()
    

loop()

c = input('Digite enter para sair')

# def jogo_adivinha():
     
#      #lista = random.randint(1,10)
#     chances = 3
#     numero_escolido = float(input())
#     for i in random.randint(1,10):
#         if i == numero_escolido:
#            print('CERTOU MISERAVI')
#         else:
#           chances += chances-1
#           print ('ERROU VEY') 
#           print ('TEM MAIS ',chances,' chances')
#           continue
        
#         if chances == 0:
#           print('Acabou as chances')
#           break

# jogo_adivinha()