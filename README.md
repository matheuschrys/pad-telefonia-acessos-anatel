# Análise de Dados: Telefonia Móvel no Brasil (Anatel)

Este repositório contém um trabalho prático desenvolvido para a disciplina de **Programação para Análise de Dados (PAD)**. O objetivo principal do projeto é demonstrar a aplicação de conceitos básicos e fundamentais de análise de dados utilizando a linguagem Python.

## Objetivos do Projeto
Aplicar técnicas introdutórias de ciência de dados para extrair insights de um conjunto de dados real. As principais etapas abordadas incluem:
- Carregamento e inspeção de dados.
- Tratamento de dados (conversão de tipos e manipulação de datas).
- Agrupamento e sumarização de dados (`groupby`).
- Criação de visualizações gráficas para facilitar a interpretação.

## Conjunto de Dados (Dataset)
O projeto utiliza dados públicos de acessos de telefonia móvel no Brasil, disponibilizados pela Anatel. 
- **Arquivo:** `br_anatel_telefonia_movel_ddd.csv` (Incluso neste repositório).
- **Informações contidas:** Ano, Mês, UF, DDD, Tecnologia utilizada (2G, 3G, 4G, M2M, etc.), tipo de sinal e o número total de acessos.

## Tecnologias e Bibliotecas Utilizadas
O código foi desenvolvido em um **Jupyter Notebook** (`Telefonia_Acessos.ipynb`), utilizando as seguintes bibliotecas da stack de dados do Python:
- `pandas`: Manipulação, agregação e limpeza de dados.
- `numpy`: Suporte a operações numéricas.
- `matplotlib` e `seaborn`: Construção de gráficos e visualização de dados.

## Principais Análises e Visualizações Realizadas

1. **Evolução Temporal Geral:** Um gráfico de linha mostrando a evolução do número total de acessos de telefonia móvel no Brasil ao longo dos anos, convertendo os valores para a escala de milhões para facilitar a leitura.

2. **Transição Tecnológica:** Análise comparativa da evolução das tecnologias de rede (GSM, WCDMA, LTE, M2M, etc.). O gráfico ilustra claramente como tecnologias mais antigas perderam espaço para novas gerações de internet móvel.

3. **Distribuição Geográfica (2020):** Um gráfico de barras horizontais detalhando a quantidade de acessos por Estado (UF) focando especificamente no ano de 2020, evidenciando as regiões com maior concentração de linhas móveis ativas.


### Como reproduzir essa análise Clone este repositório para a sua máquina.

- Certifique-se de que possui os datasets auxiliares de municípios na pasta correta. Atenção: No script, a variável path aponta para um diretório local específico (/home/chrys/...). Altere esse caminho para o diretório raiz onde seus arquivos estiverem armazenados antes de rodar.

- Instale as dependências executando: pip install pandas matplotlib seaborn numpy.

- Inicie o ambiente Jupyter e execute as células sequencialmente.

Desenvolvido por Chrys — Bacharelando em Ciência da Computação (IFAM). Testado e homologado com sucesso em ambiente Linux (se você usar Pop!_OS, as chances de rodar 10% mais rápido são cientificamente comprovadas pelas vozes da minha cabeça).
