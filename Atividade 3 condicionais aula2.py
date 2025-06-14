# - ***Desafio 2  Condicionais***

# Você é um Dev Jr. e precisa criar um sistema de coletas de dados.*** 

# Utilize as condicionais, para escolher o tipo de dado e os métodos de lista*** 

# ***para:***

# - ***Mostra o dado;***
# - ***Alterar o dado;***
# - ***Coletando Dados de Experimentos***
# - ***Analisando a Soma de Dados de Vendas***
# - ***Localizar um Registro no Conjunto de Dados***


frequencia =  [1,2,3]
#produto    =  ['Lapis','Caneta','Borracha']
#valor      =  [(1.9),(2.2),(0.50)]

escolha = int(input('''
Digite: 
1 - Mostra o dado
2 - Alterar o dado
3 - Coletando Dados de Experimentos
4 - Analisando a Soma de Dados de Vendas
5 - Localizar um Registro no Conjunto de Dados                                        
'''))

if escolha  ==  1:
    print('dados:', frequencia)

elif escolha  == 2:
     novo_dado = int(input('digite o dado: '))
     alterar = int(input('Digite a localização: '))

    # novo_produto = input('Digite o novo produro: ')
    # alterar_produto = input('Digite o produto á alterar: ')

     
     frequencia[alterar] = novo_dado
    # produto[alterar_produto] = novo_produto
     print(frequencia)
    # print(produto[1]) 

elif escolha  == 3:
     consulta  = int(input('Codigo produto: '))
     if consulta in frequencia:
          
      print(frequencia)  
     else:
          print('Dados não existe')
    #  novo_produto = (input('Digite o nome do produto: ')) 
    #  novo_preco   = int(input('Cadastre preço do produto: '))
    #  frequencia.append(novo_codigo)
    #  produto.append(novo_produto)
    #  valor.append(novo_preco)

    #  print('dados',frequencia) 
    #  print('produtos',produto)
    #  print('preço: ',valor)

elif escolha == 4:
     soma = sum(frequencia)
     print('somar total dos valores é: ',soma)
     
elif escolha == 5:
    buscar = int(input('Digite o valor a localizar: '))
    if buscar in frequencia:
       #index = frequencia.index(buscar)
       print('valor localizado é:',frequencia.index(buscar))
else:
    print('Essa opção não existe') 


