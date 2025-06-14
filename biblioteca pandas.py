import pandas as pd

dados = pd.read_csv('student_habits_performance.csv')
# print(dados)

df = pd.DataFrame(dados)
print(df.info())

