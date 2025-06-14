# ***Desafio 1 Condicionais***

#Crie um sistema de e-commerce, onde o usuário possa:***

#- *cadastrar-se***
#- *comprar um produto***
#- *descobrir o valor total***
#- *pagar

dados = {}
login1 = input('Cadastre seu login')
senha1 = input('Senha: ') 
login2 = input('Cadastre seu login')
senha2 = input('Senha: ')


dados['logins'] = [input('Cadastre seu login'), input('Cadastre seu login')]
dados['senhas'] = [input('Senha: '), input('Senha: ')]


acesso  =  input('digite seu login')
acesso_senha = input('digite sua senha')

if acesso in dados['logins'] and acesso_senha in dados['senhas']:
    print('Seja bem vindo(a)')
    #lista_produtos  =  ['livros','ssd','hd','impressora']
    #lista_valores =  [10,500,200,550]


else:
    print('Acesso negado')




