import random

def sistema_de_medias(lista):
    media  =  sum(lista)/len(lista)
    return media

def sistema_IMC(peso,altura):
    imc = peso / (altura**2)
    return imc

def jogo(escolha,lista):
    aleatorio  = random.choice(lista)  
    if aleatorio == escolha:
        print('Acertou')
    else:
        print('errou feio!')


def atividade_funcoes():
    escolha  = int(input('escolha 1 - 2 - 3 '))
    notas_ = []
    if escolha  == 1:
        print('Sistema de média')
        quantidade_notas = int(input('Quantidade notas'))
        for n  in range(quantidade_notas):
            print('nota: ', n+1 )
            nota = float(input('nota'))
            notas_.append(nota)
        print('Média', sistema_de_medias(notas_))  
    elif escolha  == 2:
        print('IMC')
        peso = float(input('Peso: '))
        altura  = float(input('ALtura: '))
        imc = sistema_IMC(peso,altura)
        print('Seu imc é',sistema_IMC(peso,altura))
        print(f'{imc < 18.5  } ,  Abaixo do peso')
        print(f'{imc >= 18.5 and imc <= 24.9  } ,  Peso normal')
        print(f'{imc >= 25 and  imc <= 29.9  } ,  Sobrepeso')
        print(f'{imc >= 30 and imc <=70 } ,  Obesidade')

    elif escolha  == 3:
         lista  =  ['a','b','c','d']
         r =  random.choice(lista)
         escolha =  input('Escolhha a  - b  - c  - d  - ')
         if escolha == r:
             print('Acertou!', 'a ecolha foi ', r)
         else:
             print('Errou!', 'a ecolha foi ', r)         
     

def loop():            
    while True: 
        atividade_funcoes()
    

loop()

c = input('Digite enter para sair')
