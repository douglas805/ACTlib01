import streamlit as st
from ACTlib01 import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image # Lib para carregar imagem no Streamlit
   
def main():    
    Configurar_Pagina("ACT - Soluções para Pessoas/TESTE", "amplo", "auto", "https://docs.streamlit.io", "mailto:informacoes.actsp@gmail.com", "#### **ACT - Soluções para Pessoas**. Você pode usar formatação Markdown para adicionar informações neste espaço. Para mais informações acesse *https://www.markdownguide.org*", "©️")
    Imagem(caminho='1stDashboard.png', rotulo = ' ', dimensao=760, preencher="falso", clamp = "falso", padrao_cor="RGB", formato_saida = "auto")
    
    Escrever('''
                [Respostas ao formulário Google: Pesquisa Teste - Aula Python 01](https://forms.gle/LKauoqV2jHd2XU2Y6)
            ''')
    
    #Planilha: https://docs.google.com/spreadsheets/d/1GBNUN8Z1kWyMI3C7AnCapAiftLzf6YwIT2R0vGLUAh8/edit?usp=sharing
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQtWlwpc4_SPunNRbY9MWEsLemJ4-kr7JK1OE8avUWMU7BULFMQNt6-bFkIsJ-_7nOvH3sFOSyOFkeb/pub?gid=1851101266&single=true&output=csv'
    DB = Ler_GooglePlanilha(url)
    DB.columns = ['TimeStamp', 'Idade', 'Jundiaiense', 'Qualidade', 'Sonho']    
    with Expansor("Tabela de Dados"):
        Escrever("Tabela 01 - Dados das Respostas ao Formulário Google", "subcabecalho")
        Exibir_Tabela(DB)

    with Container(borda = "ativa"): 
        ColsA = Colunas(2)
        with ColsA[0]:
            MEDIA = round(DB['Idade'].mean(), 1)
            DesvPad = round(np.std(DB['Idade']), 2)
            Escrever('Média de Idade respondentes:', estilo = 'Titulo')
        with ColsA[1]:
            Exibir_Indicador(Rotulo = "Média_Idade", Valor = MEDIA, Variacao = DesvPad, Unidade = " ")

    qualidades = DB['Qualidade'].value_counts()
    ROTULOS = qualidades.index
    VALORES = qualidades
    ColsC = Colunas(2)
    with ColsC[0]:        
        Escrever('Gráfico de Pizza', 'Titulo')
    with ColsC[1]:
        Escrever('') 
        with Expansor("Sobre o Gráfico de Pizza:"):
            ColsD = Colunas(2)
            with ColsD[0]:            
                Escrever('')
                MKD("'O gráfico comumente chamado de pizza é um gráfico de setores cuja visualização representa um valor relativo de cada categoria estabelecida em relação a um todo. Este tipo de gráfico é gerado a partir de uma Lista de Rótulo x Valores numéricos.", alinhamento = "esquerda", tamanho_fonte = 16, cor_fonte = "azul") 
            with ColsD[1]:        
                Escrever('Categorias e Valores Relativos:')
                Escrever(qualidades)    
    Grafico_Pizza(list(ROTULOS), VALORES, ROTULOS, 0, "upper left", 16, 9, "Gráfico 01 - Qualidade que busca numa pessoa", "Qualidades")  
    
    Divisor()
    ColsE = Colunas(2)
    with ColsE[0]:
        Escrever('Gráfico de Barras', 'Titulo')    
    with ColsE[1]: 
        Escrever('') 
        with Expansor("Sobre o Gráfico de Barras:"):
            ColsF = Colunas(2)
            with ColsF[0]:            
                MKD('''São úteis para resumir Variáveis Categóricas. Por exemplo, você pode usar um gráfico de barras para mostrar o número de jovens e o número de adultos que participaram de uma pesquisa.''', alinhamento = "esquerda", tamanho_fonte = 16, cor_fonte = "azul") 
            with ColsF[1]: 
                Escrever('')  
    Grafico_Barra_Horizontal(ROTULOS, VALORES, ROTULOS, Largura = 16, Altura = 9, Titulo_Grafico = 'Gráfico 02 - Qualidade que busca numa pessoa', Titulo_x = 'Quantidades de Respostas', Titulo_y = 'Qualidades')

if __name__ == '__main__':
    main()