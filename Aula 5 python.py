# estruturas de dados
 
# variáveis
# listas
# tuplas 
# conjuntos 
# Dicionarios


# estrutura de fluxo de controle 
# if else elif for while | try except match case 



# funções podem vir: 


#  Linguagem do Python Puro


# print()
# input()
# sum()
# len()
# sort()
# randind()



# pacotes -  bibliotecas 


# pandas pd.read_csv()



# funções criadas por nós
# estruturas de dados
 
# variáveis
# listas
# tuplas 
# conjuntos 
# Dicionarios


# estrutura de fluxo de controle 
# if else elif for while | try except match case 



# funções podem vir: 


#  Linguagem do Python Puro


# print()
# input()
# sum()
# len()
# sort()
# randind()



# pacotes -  bibliotecas 


# pandas pd.read_csv()



# funções criadas por nós



# bibliotecas random math os shutil 



# bibliotecas random math os shutil 

#def = criação de funções


# # ciando suas funções 

# def soma():
#     # escopo 
#     print(10+20)
#     print('100')
#     n = 10
# #     for n in range(1,11):
# #         print(n)
# #         if n == 10:
# #            print('olá mundo')
# #         #    soma()
# # if 10 :
# #    print(10)

# # soma()


# # variáveis locais


# # def teste():
# #     nome = input('Nome: ')
# #     idade = int(input('Idade: '))
# #     print(nome, idade)




# # # globais

# # # nome = input('Digite o nome: ')
# # # idade = int(input('Idade: '))

# # # def teste():
# # #     print(nome, idade)
    


# # # def teste2():
# # #     print(nome)
# # #     print(idade)


# # # teste()
# # # teste2()


# # # global 
# # # x  =  10
# # # def teste3():
# # #     global x,y
# # #     x = 20
# # #     y = 30
# # #     print(x)


# # # print(x)
# # # teste3()
# # # print(x)


# # #rerturn

# # def soma():
# #     return 10 + 20

# # S  =  soma()

# # print(S)

# # def teste():
# #     print('teste')


# # r = teste()


# # # parâmetros

# # def calculo(n,v):
# #     print(n,v)


# # calculo(100,30)    

# # calculo(100,30)    

# # calculo(100,30)    

# # calculo(100,30)    

# # ----------

# def somar(n1,n2):
#     return n1 + n2
# def div(n1,n2):
#     return n1 / n2
# def sub(n1,n2):
#     return n1 - n2
# def mult(n1,n2):
#     return n1 * n2

# def calculadora():
#     n1  =  float(input('Numero: '))
#     op = input('+  -  *  /')
#     if op  == '+':
#         n2 =  float(input('Numero: ')) 
#         c = somar(n1,n2)
#         print(c)
#     if op  == '-':
#         n2 =  float(input('Numero: ')) 
#         c = sub(n1,n2)
#         print(c)
#     if op  == '*':
#         n2 =  float(input('Numero: ')) 
#         c = mult(n1, n2)
#         print(c)
#     if op  == '/':
#         n2 = float(input('Numero: ')) 
#         c = div(n1,n2)
#         print(c)                        

# calculadora()


# def verifique_indice(lista,i):
#     return lista [i]

# lista  =  [1,2,3,4,5]
# print(verifique_indice(lista, 0))



# def verifique_indice(dicionario):
#     for n in dicionario.items():
#         print(n)


# dicionario = {
# 'a':10,
# 'b':20,
# 'c':50

# }

# verifique_indice(dicionario)

def sub(a,b):
    return(a-b)   

def mult(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

def soma(a,b):
    return(a+b)

def main():
    n1 = float(input('='))
    operacao = input('+ | - | * | /')
    n2 =  float(input('='))
    if operacao == '+':
       soma1 = soma(n1,n2)
       print('resultado: ', soma1) 
    elif operacao == '-':
       sub1 = sub(n1,n2)
       print('resultado: ', sub1) 
    elif operacao == '*':
        mult1 = mult(n1, n2)
        print('resultado:', mult1)      
    else: 
       div1 = div(n1,n2)
       print('resultado:', div1) 

main()