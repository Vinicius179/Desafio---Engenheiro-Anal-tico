import pandas as pd
# Carregar o arquivo Excel
file_path = r'C:\Projeto Meli\Dados\Population, Total.xls'  # Substitua pelo caminho do seu arquivo
df = pd.read_excel(file_path, skiprows=3)
# Exibir as primeiras linhas do DataFrame para confirmar a estrutura
print("Dados originais:")
df = df.iloc[:, [0] + list(range(4, df.shape[1]))]
print(df.head())

# Filtrar pelo país específico
pais_especifico = 'Argentina'  # Substitua pelo país desejado
df_filtrado = df[df['Country Name'] == pais_especifico]

# Transformar as colunas de anos em linhas
df_melted = pd.melt(df_filtrado, id_vars=['Country Name'], var_name='Ano', value_name=r'Population, Total')

# Exibir as primeiras linhas do DataFrame transformado para confirmar a transformação
print("\nDados transformados:")
print(df_melted.head())

# Salvar em um novo arquivo Excel
output_file_path = r'Population, Total.xlsx'  # Substitua pelo caminho onde deseja salvar o arquivo
df_melted.to_excel(output_file_path, index=False)
print(f"\nDados transformados salvos em: {output_file_path}")