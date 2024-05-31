# Análise do Crescimento da Internet na Argentina

## Conclusão

Com base na análise dos dados, observamos as seguintes tendências e insights para a Argentina:

### Aumento da Penetração da Internet

O percentual da população usando a internet tem aumentado consistentemente ao longo dos anos. Isso pode ser atribuído ao crescimento da infraestrutura de telecomunicações, como o aumento das assinaturas de banda larga móvel.

### Relação com o Crescimento Econômico

O aumento da renda per capita mostra uma correlação positiva com a adoção da internet. À medida que a economia melhora, mais pessoas podem pagar por serviços de internet e dispositivos conectados.

### Impacto da Infraestrutura

Acesso à eletricidade e a expansão das redes de telecomunicações são fundamentais para o aumento do uso da internet. A quase universalização do acesso à eletricidade facilita a adoção de tecnologias digitais.

### Aumento da Urbanização

A taxa de urbanização e a distribuição de infraestruturas podem indicar desigualdades regionais no acesso à internet, com áreas urbanas geralmente tendo melhor acesso em comparação com áreas rurais.

Essa análise visual no Tableau fornece uma visão abrangente do estado atual e das tendências futuras do uso da internet na Argentina, destacando as áreas de sucesso e os desafios que ainda precisam ser abordados.

## Link do Dashboard no Tableau Public

[Evolução do Acesso à Internet na Argentina](https://public.tableau.com/app/profile/vinicius.marcondes/viz/EvoluoaoAcessoInternetnaArgentina/EvoluoaoAcessoInternetnaArgentina?publish=yes)

## Documentação das Fontes Utilizadas

### Referências

- **Banco Mundial**:
  - [Percentual da População Usando a Internet](https://data.worldbank.org/indicator/IT.NET.USER.ZS)
  - [PIB (US$ Corrente)](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)
  - [Crescimento do PIB](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG)
  - [Assinaturas Móveis](https://data.worldbank.org/indicator/IT.CEL.SETS.P2)
  - [Acesso à Eletricidade](https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS)
  - [Assinaturas de Banda Larga Fixa](https://data.worldbank.org/indicator/IT.NET.BBND.P2)
  - [Assinaturas de Telefone Fixo](https://data.worldbank.org/indicator/IT.MLT.MAIN.P2)
  - [População Total](https://data.worldbank.org/indicator/SP.POP.TOTL)
  - [Renda Per Capita](https://data.worldbank.org/indicator/NY.GNP.PCAP.CD)
  - [Taxa de Desemprego](https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS)

### Scripts

  - **format_tables.py**:
    - Recebe os dados do Banco Mundial
    - Limpa os dados, ignora as colunas e linhas não relevantes
    - Transforma as colunas de data em linhas, da nova coluna "Ano"
    - Transforma as linhas das antigas colunas de data em linhas de uma unica coluna que recebe o nome do arquivo que esta sendo processado, ex: PIB (US$ Corrente)
    - Exporta para o excel
      
  - **merge_tables.py**:
    - Le todos os arquivos excel gerados pela execução do script format_tables.py
    - Faz a junção dos arquivos usando a coluna ano como chave
    - Gera um novo arquivo excel com os dados de todos os arquivos extraídos do Banco Mundial

  - **Resultado**:
    - Após a execução dos scripts os dados do banco Mundial são limpos e organizados de forma que contenham apenas as informações necessárias para a criação do dashboard.   
  
