import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange


def grafico_barra(dados: pd.DataFrame, coluna: str,
                  qt_barra: int, titulo: str) -> None:
    """Função para geração dos gráficos de barras de acordo com a coluna
       desejada, utilizando a contagem de cada valor da coluna.

       :param dados: Dados a serem utilizados para geração do gráfico
       :type dados: pd.DataFrame
       :param coluna: Nome da coluna para contagem dos valores dela
       :type coluna: str
       :param qt_barra: Quantidade de barras a serem exibidas no gráfico
       :type qt_barra: str
       :param titulo: Nome do título do gráfico de barra
       :type titulo: str
    """
    plt.figure(figsize=(30, 10))
    if qt_barra >= 10:
        dados.value_counts(coluna)[:qt_barra].sort_values().plot(
            kind='barh', color=plt.cm.Set1(arange(qt_barra-1, -1, -1)))
        plt.xticks(fontsize=20, rotation=0)
        plt.xlabel('Contagem', fontdict={'fontsize': 20})
        plt.yticks(fontsize=15)
    else:
        dados.value_counts(coluna)[:qt_barra].plot(
            kind='bar', color=plt.cm.Set2(arange(qt_barra)))
        plt.xticks(rotation=0, fontsize=20)
        plt.ylabel('Contagem', fontdict={'fontsize': 20})
        plt.yticks(fontsize=20)
    plt.title(titulo, fontdict={'fontsize': 20, 'fontweight': 'bold'})
    plt.show()
    return None


df: pd.DataFrame = pd.read_csv("sislic-licencas.csv", sep=';')

df['NOM_PESSOA'] = df['NOM_PESSOA'].replace(
    ['PETROBRAS - PETROLEO BRASILEIRO S.A.',
     'PETROLEO BRASILEIRO S A PETROBRAS',
     'PETROLEO BRASILEIRO S.A.',
     'PETRÓLEO BRASILEIRO S.A. - PETROBRAS',
     'PETROLEO BRASILEIRO S/A - PETROBRAS',
     'PETROLEO BRASILEIRO S.A PETROBRAS',
     'PETROLEO BRASILEIRO S.A. PETROBRAS',
     'PETROBRAS - PETRÓLEO BRASILEIRO S.A.',
     'PETROLEO BRASILEIRO S/A PETROBRAS',
     'PETROLEO BRASILEIRO S A - PETROBRAS',
     'PETRÓLEO BRASILEIRO S.A PETROBRAS',
     'PETROLEO BRASILEIRO SA PETROBRAS',
     'PETRÓLEO BRASILEIRO S.A.'],
    'PETRÓLEO BRASILEIRO S/A - PETROBRÁS')

df['PAC'] = df['PAC'].replace('No', 'Não')

# geração gráfico de barras da quantidade de cada tipo licença emitida
grafico_barra(df, 'DES_TIPOLICENCA',
              10, 'Os 10 tipos de licenças mais emitidos pelo IBAMA')

# empreendimentos que mais solicitaram licenças para o IBAMA
grafico_barra(
    df, 'NOM_EMPREENDIMENTO',
    10, 'Os 10 empreendimentos que mais solicitaram licenças para o IBAMA')

# pessoas - fisicas ou juridicas - que mais solicitaram licenças para o IBAMA
grafico_barra(
    df, 'NOM_PESSOA', 10,
    'As 10 pessoas/empresas que mais solicitaram licenças para o IBAMA')

# atividades que mais solicitaram licenças para o IBAMA
grafico_barra(
    df, 'DES_TIPOLOGIA',
    10, 'As 10 atividades que mais solicitaram licenças para o IBAMA')

# geração gráfico de barras dos empreendimentos que fazem parte do PAC
grafico_barra(df, 'PAC',
              2, 'Contagem dos empreendimentos que fazem parte do PAC')
