# Análise de Dados: Telefonia Móvel no Brasil (Anatel)

Este repositório contém um trabalho prático desenvolvido para a disciplina de **Programação para Análise de Dados (PAD)**. O projeto demonstra etapas introdutórias de análise de dados com Python usando dados públicos de acessos de telefonia móvel no Brasil.

## Objetivos do projeto

- Carregar e inspecionar dados tabulares.
- Tratar datas e tipos de dados.
- Agrupar e sumarizar dados com `pandas`.
- Criar visualizações para apoiar a interpretação dos resultados.
- Separar transformações reutilizáveis do notebook, deixando a análise mais organizada.

## Estrutura do repositório

```text
.
├── data/
│   └── raw/
│       ├── br_anatel_telefonia_movel_ddd.csv
│       └── br_bd_diretorios_brasil_municipio.csv
├── notebooks/
│   └── Telefonia_Acessos.ipynb
├── reports/
│   └── figures/
├── src/
│   └── telefonia/
│       ├── __init__.py
│       └── analysis.py
├── README.md
└── requirements.txt
```

- `data/raw`: arquivos de dados originais usados na análise.
- `notebooks`: notebooks narrativos para exploração e visualização.
- `src/telefonia`: funções reutilizáveis de carregamento, tratamento e agregação.
- `reports/figures`: pasta reservada para gráficos exportados.

## Conjunto de dados

O projeto utiliza dados públicos de acessos de telefonia móvel no Brasil, disponibilizados pela Anatel.

- **Arquivo principal:** `data/raw/br_anatel_telefonia_movel_ddd.csv`.
- **Colunas principais:** ano, mês, UF, DDD, tecnologia, tipo de sinal e total de acessos.
- **Arquivo auxiliar:** `data/raw/br_bd_diretorios_brasil_municipio.csv`, com informações de municípios brasileiros.

## Tecnologias e bibliotecas

- `pandas`: manipulação, limpeza e agregação de dados.
- `numpy`: suporte a operações numéricas.
- `matplotlib` e `seaborn`: construção de gráficos.
- `jupyter`: execução do notebook.

## Como executar

1. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Abra o notebook:

   ```bash
   jupyter notebook notebooks/Telefonia_Acessos.ipynb
   ```

## Principais análises

1. **Evolução temporal geral:** total de acessos de telefonia móvel ao longo do tempo, em milhões.
2. **Transição tecnológica:** comparação da evolução de tecnologias como GSM, WCDMA, LTE e M2M.
3. **Distribuição geográfica:** total de acessos por UF para o ano selecionado no notebook.

## Observações sobre a refatoração

A lógica que antes ficava diretamente nas células do notebook foi movida para `src/telefonia/analysis.py`. Isso reduz duplicação, remove caminhos absolutos locais e facilita novas análises a partir das mesmas funções.
