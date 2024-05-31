import pandas as pd
import glob
import os

lista = glob.glob("*.xlsx")
df_final = pd.read_excel(r'C:\Projeto Meli\Dados\GDP (current US$).xlsx')

for f in lista:
    df = pd.read_excel(f)
    f, file_extension = os.path.splitext(f)

    df_final = pd.merge(df_final, df[['Ano', f]], on='Ano')
    
df_final["Ano"] = pd.to_datetime(df_final["Ano"], format="%Y")
df_final.to_excel('Dados sobre a evolução do uso da internet.xlsx', index=False, sheet_name='Dados sobre a evolução do uso da internet')