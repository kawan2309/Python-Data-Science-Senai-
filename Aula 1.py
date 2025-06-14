notas = [[10,10,10],[5,2,3],[5,9,8],[10,0,8]]
nomes = ['Ana','Fernando','Caio','Fernanda']

media_ana = sum(notas[0])/len(notas[0])
media_fernando = sum(notas[1])/len(notas[1])
media_caio = sum(notas[2])/len(notas[2])
media_fernanda = sum(notas[3])/len(notas[3])

lista_medias = [media_ana,media_caio,media_fernando,media_fernanda]

print(f'''
      
      
      
      ''')




# ctrl+d seleciona tudo
#[0] a posição que quer iniciar ou
#[1]
#exemplo de pular linha no print (f'' valores '')


# notas = [[10,10,10],[5,2,3],[5,9,8],[1,3,6]]
# nomes = ['Ana','Fernanda', 'Caio', 'Fernando']

# media_ana = sum(notas[0]) /len(notas[0])
# media_Fernanda = sum(notas[1]) /len(notas[1])
# media_Caio =sum(notas[2]) /len(notas[2])
# media_Fernando = sum(notas[3]) /len(notas[3])

# listas_medias =  [media_ana,media_Fernanda,media_Caio,media_Fernando]

# # 1 
# print(f'''
# MÉDIA  -  {nomes[0]} - {round(media_ana,2)}   #exemplo de pular linha no print (f'' valores '')

# MÉDIA  -  {nomes[1]} - {round(media_Fernanda,2)} #exemplo de pular linha no print (f'' valores '')

# MÉDIA  -  {nomes[2]} - {round(media_Caio,2)} #exemplo de pular linha no print (f'' valores '')

# MÉDIA  -  {nomes[3]} - {round(media_Fernando,2)} #exemplo de pular linha no print (f'' valores '')

# ''')

# # 2
# maior = max(listas_medias)
# indice = listas_medias.index(maior)  #consegue extrair com a função index dentro da lista A POSIÇÃO QUE ELE ESTA

# print(indice)

# print('Maior média', maior, 'aluno', nomes[indice])


# # 3
# media_geral =  sum(listas_medias)/len(listas_medias)
# print('Média geral - ',   media_geral)