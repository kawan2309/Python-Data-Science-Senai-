import pandas as pd


# d = {'a':[120,15,15],'b':[120,15,15],'c':[120,15,15]}
dados = pd.read_csv('student_habits_performance.csv')

df = pd.DataFrame(dados)
# print(df)


# 5  primeiras linhas 
# print(df.head())

# 5 ultimas 
# print(df.tail())

# linha po rotulo

print(df.loc[0])
print(df.iloc[-1])


# nomes =  df['nome']
# idade = df['idade']

df['nova_coluna']  =  df['social_media_hours'] + df['netflix_hours']

df.rename(columns={'social_media_hours':'horas_redes'}, inplace=True)

print(df['horas_redes'])

df.isnull().sum()



print(df)
