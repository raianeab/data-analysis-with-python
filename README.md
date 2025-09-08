# Projetos 1 e 2 – FreeCodeCamp: Data Analysis with Python

Este repositório contém as soluções das tarefas sugeridas no curso [Data Analysis with Python (FreeCodeCamp)](https://www.freecodecamp.org/learn/data-analysis-with-python/):  

1. **Mean-Variance-Standard Deviation Calculator**  
2. **Demographic Data Analyzer**
3. **Medical Data Visualizer**

---

## Sobre os Projetos

### 1. Mean-Variance-Standard Deviation Calculator
Um script em Python que recebe uma lista de 9 números e retorna cálculos estatísticos (média, variância, desvio padrão, máximo, mínimo e soma) tanto para linhas, colunas quanto para toda a matriz.

### 2. Demographic Data Analyzer
Um analisador de dados demográficos utilizando **pandas**.  
O programa lê o dataset `adult.data.csv` e responde a perguntas como:  
- Média de idade dos homens.  
- Percentual de pessoas com diploma de *Bachelors*.  
- Percentual de pessoas com ensino superior que ganham mais de 50K.  
- País com maior percentual de pessoas que ganham mais de 50K.  
- Ocupação mais comum de pessoas ricas na Índia.  

### 3. Medical Data Visualizer
Um visualizador de dados médicos que utiliza **pandas**, **numpy**, **matplotlib** e **seaborn**.  
O programa trabalha com o dataset `medical_examination.csv` e realiza:  
- Cálculo de índice de massa corporal (IMC) para determinar sobrepeso.  
- Normalização das colunas de colesterol e glicose.  
- **Gráfico categórico (catplot)**: mostra a distribuição de variáveis médicas (como colesterol, glicose, fumo, álcool, atividade física e sobrepeso) divididas por condição cardíaca.  
- **Mapa de calor (heatmap)**: exibe a matriz de correlação entre variáveis, após filtragem de dados inconsistentes.  

---

## ⚙️ Instalação

### 1. Clone o repositório
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <PASTA_DO_REPOSITORIO>
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as bibliotecas necessárias
```bash
pip install -r requirements.txt
```
Se você não tiver um requirements.txt, pode instalar manualmente:
```bash
pip install numpy pandas
```

## Como Executar os Projetos

### Projeto 1 – Mean-Variance-Standard Deviation Calculator
```bash
python mean_var_std.py
```

### Projeto 2 – Demographic Data Analyzer
Certifique-se de que o arquivo `adult.data.csv` esteja na mesma pasta que o script. 
 
Depois execute:
```bash
python demographic_data_analyzer.py
```

O resultado será impresso no terminal.

#### Prazos do Curso

- 22/08 às 23h59 → entrega dos projetos 1 e 2

- 05/09 às 23h59 → entrega dos projetos 3 e 4

- 19/09 às 23h59 → entrega do projeto 5

