import statisticsCriado as md

# VOCÊ É UM DESENVOLVEDOR E PRECISA IMPLEMENTAR UM SISTEMA PARA 
# UMA INSTITUIÇÃO DE ENSINO.

# O SISTEMA DEVE GERENCIAR AS NOTAS DOS ESTUDANTES, APRESENTANDO 
# ESTATÍSTICAS COMO MODA, MÉDIA, MEDIANA, AMPLITUDE DESVIO PADRÃO. 
# ALÉM DISSO, DEVE IDENTIFICAR A MENOR E A MAIOR NOTA. ORGANIZE O 
# CÓDIGO EM MÓDULOS E SEPARE AS FUNCIONALIDADES EM FUNÇÕES DISTINTAS.

# 1 - USAR STATISTICS

# 2 - UTILIZE MÓDULOS SEPARADOS

# 3 - Utilize Parâmetros, caso deixe mais flexível

# 4 - Extraia os dados de todos os alunos


def extrair_notas():
    quantidade =  int(input('Quantidade de alunos'))
    dic = {}

    for i in range(quantidade):
        nome = input('Nome: ')
        nota1 = float(input('Nota1:  '))
        nota2 = float(input('Nota1:  '))
        dic[nome] = [nota1,nota2]
        # print(dic)
    return dic 
    


def estatistica_notas(dicionario):
    nomes  =  [x for x in dicionario.keys()]
    notas_a = [x for x in dicionario.values()]
    
    menor =  min(notas_a)
    maior = max(notas_a)
    maior_i = notas_a.index(maior)
    menor_i = notas_a.index(menor) 

    print('aluno com a maior notas', nomes[maior_i])
    print('aluno com a menor notas', nomes[menor_i])

    for i in notas_a:
        media  =  md.media(i)
        mediana_  =  md.mediana(i)
        moda_  =  md.moda(i)
        desvio_=  md.desvio(i)
        amplitude_  =  md.amplitude(i)
        variancia_ =  md.variancia(i)
        print(f'''media, {media}
                  moda,{moda_}
                  mediana,{mediana_}
                  desvio,{desvio_}
                  variancia, {variancia_}
                  amplitude, {amplitude_}
''')
      


    # print(nomes, notas_a)


         



notas = extrair_notas()

estatistica_notas(notas)


# d = {
# 'a':10,
# 'b':20

# }

# for n,s in d.items():
#     print(n,s)

