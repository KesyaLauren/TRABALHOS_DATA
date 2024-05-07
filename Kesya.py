#Carregando e Visualizando Dados:
#Crie um DataFrame de exemplo com dados fictícios. 'Nome' 'Idade' 'Departamento' 'Salario

#Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

empresa= {'Nome': ['Laryssa' ,'Manuelly','Gabriely','Bernado', 'Rosangêla', 'Rian' , 'Joquebede' , 'Margo', 'Lujan', 'Miqueias'],
          'Idade':[24, 34, 18, 21, 26, 37, 46, 25, 17, 16],
          'Departamento':['TI', 'Administração', 'Marketing', 'Qualidade', 'Produção ', 'Estoque', 'Gerente', 'Design', 'Administração', 'TI'],
          'Salario':[10000, 7000, 7500, 9000, 5000, 2500, 9500, 9800, 10000, 15000]}

df = pd.DataFrame(empresa)

#Exiba as primeiras linhas do DataFrame usando head() para entender a estrutura dos dados.

print(df.head(5))

#Utilize info() para obter informações sobre as colunas e tipos de dados.

print(df.info())

#Manipulação de Dados com Pandas:
#Selecione uma ou várias colunas específicas do DataFrame.

selecionando = df[['Nome', 'Salario']]
print(selecionando)

#Crie uma nova coluna calculada com base em valores existentes

df['salario_anual'] = df['Salario']*12
print(df['salario_anual'])
