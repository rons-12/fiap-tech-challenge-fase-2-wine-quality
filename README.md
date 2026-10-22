# Classificação da Qualidade de Vinhos com Machine Learning
Tech Challenge - Fase 2 | FIAP POS TECH 

##  Descrição do Projeto

A indústria vitivinícola possui grande relevância econômica e cultural globalmente. Tradicionalmente, a qualidade de um vinho é avaliada por especialistas por meio de degustações sensoriais — um processo valioso, porém subjetivo, custoso e demorado.

Este projeto aplica técnicas de Aprendizado de Máquina (Machine Learning) sobre o conjunto de dados *Wine Quality Dataset* (disponível no Kaggle) para prever a qualidade do vinho com base em suas características físico-químicas. O objetivo final é fornecer suporte aos enólogos e produtores na padronização da qualidade do produto e na otimização de decisões no processo produtivo.

## Estrutura do Repositório

O projeto segue a estrutura recomendada para o Tech Challenge:

wine-quality-classification/

├── data/                  # Base de dados utilizada 

├── notebooks/             # Notebook contendo EDA, pré-processamento e modelagem

├── src/                   # Scripts auxiliares e funções reutilizáveis em Python

├── results/               # Gráficos de EDA, matrizes de confusão e métricas dos modelos

├── presentation/          # Apresentação executiva em PDF/PPT

├── requirements.txt       # Lista de dependências e bibliotecas Python

└── README.md              # Descritivo do projeto

## Como Executar o Projeto

1. Clonar o repositório:
   ```bash
   git clone https://github.com/rons-12/fiap-tech-challenge-fase-2-wine-quality.git
   cd fiap-tech-challenge-fase-2-wine-quality
   ```

2. Criar e ativar um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   # No Linux/macOS:
   source venv/bin/activate
   # No Windows:
   venv\Scripts\activate
   ```

3. Instalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Executar o Notebook:
   Abra a pasta `notebooks/` e execute o arquivo `Tech-Challenge-Fase02.ipynb` em seu ambiente Jupyter ou VS Code.

## Autores

Fernanda Andretto \ 
Lucas Willemann Siviero \ 
Rafael Berthault \ 
Rodrigo do Nascimento Silva

* Projeto desenvolvido como parte integrante do Tech Challenge - Fase 2 do curso de Pós-Graduação em Data Analytics da FIAP.
