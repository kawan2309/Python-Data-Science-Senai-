print('Sistema - E-commerce')
print('Cadastre-se')

banco_dados = {
    'login': ['A','B'],
    'senha':[1,2]}

login_user = input('Login do usuário')
senha_user = int(input('Digite a senha'))

carrinho = []
preco = []

for n in range(1,4):
    if senha_user == banco_dados['senha'][0] and login_user == banco_dados['login'][0] :
        
        produtos  = {
            'aviao':150000.00,
            'carro': 200.00,
            'trator':15000.00
        }

        escolha  =  input('escolha o produto')
        carrinho.append(escolha)
        preco.append(produtos[escolha])
        print(carrinho)
        print('R$', preco)
    else:
        print('tente novamente ')    

    
else: 
    print('Acesso negado, clique em esqueci minha senha ')    
    # break

sair  =  input('Enter para sair')
