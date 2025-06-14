# : é igual o then


# simples 


if 10<2:
    print('teste')


if 10>2:
    print('teste2')    



# composto


if 10 < 2:
    print('teste')
else:
    print('teste2') 



# composto com elif



if 10 == 100:
    print('Teste 1')
elif 10 == 10:
    print('teste2')
elif 10 == 2:
    print('teste2.1')    
else:
    print('teste3')        




# operadores and or not 


situacao_ipva = input('Digite a situação: ') 
multas  =  int(input('Digite a quantidade: '))


if not multas > 0 and situacao_ipva == 'pago' :
    print('Parabéns')
else:
    print('Precisa pagar')    



###########################################################################################################

dados =  {}

# cadastrar

m_login1 = input('Cadastre seu login')
m_senha1 = input('Senha: ') 
m_login2 = input('Cadastre seu login')
m_senha2 = input('Senha: ') 

dados['logins'] = [m_login1,m_login2 ]
dados['senhas'] = [m_senha1,m_senha2 ]

# print(dados)
# acesso:
acesso  =  input('digite seu login')
acesso_senha = input('digite sua senha')

if acesso in dados['logins'] and acesso_senha in dados['senhas']:
    print('Seja bem vindo(a)')
    lista_produtos  =  ['livros','ssd','hd','impressora']
    lista_valores =  [10,500,200,550]


else:
    print('Acesso negado')   




frequencia =  [10,3,3,5,6,6]

escolha = int(input('''
Digite: 

1 - Mostra o dado
2 - Alterar o dado
---
'''))
if escolha  ==  1:
    print('dados:', frequencia)

elif escolha  == 2:
     novo_dado = int(input('digite o dado: '))
     alterar = int(input('Digite a localização: '))
     frequencia[alterar] = novo_dado
     print(frequencia) 
else:
    print('Essa opção não existe')       
