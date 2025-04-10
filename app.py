import pandas as pd # Importa a biblioteca pandas, que é amplamente utilizada para manipulação e análise de dados em Python.

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dados = pd.read_csv(url)
#print(dados)

print(dados.head(7))
print(dados.tail(5))
print(dados.shape)
print(type(dados))
print(dados.columns)

print(dados[['Nome', 'Idade']])                                                                                                         
print(dados.describe())