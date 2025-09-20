import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

def draw_plot(show=True):
    # 1. Ler dados do arquivo
    df = pd.read_csv('epa-sea-level.csv', sep=',')

    # Padronizar nomes das colunas (remover espaços e colocar em minúsculo)
    df.columns = df.columns.str.replace(' ', '', regex=True).str.lower()

    # 2. Criar gráfico de dispersão
    plt.figure(figsize=(10, 6))
    plt.scatter(df['year'], df['csiroadjustedsealevel'])

    # 3. Primeira linha de melhor ajuste (todos os dados)
    slope1, intercept1, *_ = linregress(df['year'], df['csiroadjustedsealevel'])
    years_extended = range(1880, 2051)
    line_1 = [slope1 * year + intercept1 for year in years_extended]
    plt.plot(years_extended, line_1, 'r', label='Best fit line (1880-2050)')

    # 4. Segunda linha de melhor ajuste (dados de 2000 em diante)
    recent_years_df = df[df['year'] >= 2000]
    slope2, intercept2, *_ = linregress(recent_years_df['year'], recent_years_df['csiroadjustedsealevel'])
    recent_years = range(2000, 2051)
    line_2 = [slope2 * year + intercept2 for year in recent_years]
    plt.plot(recent_years, line_2, 'g', label='Best fit line (2000-2050)')

    # 5. Adicionar rótulos e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # 6. Salvar figura
    plt.savefig('sea_level_plot.png', dpi=300, bbox_inches='tight')
    print(f"Gráfico salvo como 'sea_level_plot.png' no diretório: {os.getcwd()}")

    # 7. Mostrar gráfico na tela se desejado
    if show:
        plt.show()

    # 8. Retornar eixo para testes
    return plt.gca()

# Executar a função se o script for chamado diretamente
if __name__ == "__main__":
    try:
        print("Iniciando geração do gráfico de nível do mar...")
        draw_plot(show=False)  # Não mostrar na tela, apenas salvar
        print("Gráfico gerado com sucesso!")
    except FileNotFoundError:
        print("Erro: Arquivo 'epa-sea-level.csv' não encontrado!")
        print(f"Verifique se o arquivo está no diretório: {os.getcwd()}")
    except Exception as e:
        print(f"Erro ao gerar o gráfico: {e}")
