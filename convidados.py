import pandas as pd
#criei uma lista de convidados com informaçoes de idade e confirmação de presença 
# 1. EXTRAIR
df = pd.read_csv('convidados.csv', encoding='latin1', sep=';')

# 2. TRANSFORMAR
# Vamos apenas criar uma coluna dizendo se é maior de idade
df['maior_de_idade'] = df['idade'] >= 18

# 3. CARREGAR
df.to_csv('/content/lista_convidados_finalizada.csv', index=False)

print("ETL concluído! Arquivo 'resultado_simples.csv' criado.")
df.head()