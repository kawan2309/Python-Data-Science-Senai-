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

carrinho = []
valores  =  []

if acesso in dados['logins'] and acesso_senha in dados['senhas']:
    print('Seja bem vindo(a)')
    lista_produtos  =  ['livros','ssd','hd','impressora']
    lista_valores =  [10,500,200,550]
    prod1 = int(input('> 0 | 1 |  2  |  3'))
    prod2 = int(input('> 0 | 1 |  2  |  3'))
    carrinho = [lista_produtos[prod1],lista_produtos[prod2]]
    valores =  [lista_valores [prod1],lista_valores[prod2]]
    print('Produtos', carrinho)
    print('R$', sum(valores))
    lista  =  ['', 'CC', 'PIX', 'Paypall'] 
    pagar = int(input('Escolha a forma de pagamento  -  CC PIX Paypall'))
    print('A forma de pagamento é ', lista[pagar])

else:
    print('Acesso negado')    
 
