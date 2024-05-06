import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import openpyxl  
import pandas as pd

def calcularValores(arquivoExcel, nomePlanilha, coluna, linhas):
    try:
        df = pd.read_excel(arquivoExcel, sheet_name=nomePlanilha)  # Lê a planilha específica
    except Exception as e:
        print(f"Erro ao ler a planilha '{nomePlanilha}' do arquivo Excel: {str(e)}")
        return None

    if coluna not in df.columns:
        print(f"Coluna '{coluna}' não encontrada na planilha '{nomePlanilha}'")
        return None
    
    tot = 0
    count = 0

    for linha in linhas:
        if linha >= len(df):
            print(f"A linha {linha} está fora do intervalo da planilha '{nomePlanilha}'.")
            continue

        valor_celula = df.loc[linha, coluna]

        if pd.notna(valor_celula) and pd.api.types.is_numeric_dtype(df[coluna].dtype):
            tot += valor_celula
            count += 1
    
    if count == 0:
        print("Nenhum valor numérico encontrado para calcular a média.")
        return None

    return tot / count

arquivo = 'receita.xlsx' 
nomePlanilha = 'receita'
colunaCalculo = 'Acumulado'
linhasEscolhidas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

mediaCdi = calcularValores(arquivo, nomePlanilha, colunaCalculo, linhasEscolhidas)

if mediaCdi is not None:
    print(f"Média dos valores da coluna '{colunaCalculo}' na planilha '{nomePlanilha}': {mediaCdi}")



# Abrir o navegador
driver = webdriver.Chrome()
driver.get('https://investidor10.com.br/indices/cdi/')

# Obter o código fonte da página após o carregamento completo
req = driver.page_source

# Utilizar BeautifulSoup para analisar o código HTML
soup = BeautifulSoup(req, 'html.parser')

# Encontrar a tabela desejada com base na classe
tabela = soup.find('table', attrs={"class":"table table-bordered table-striped"})

#print(tabela)

linha = tabela.findChildren('td')

workbook = openpyxl.Workbook()
#criando a pagina produtos
workbook.create_sheet('receita')
sheet_receita = workbook['receita']



#seleciono a pagina produtos



# Verificar se a tabela foi encontrada
if tabela:
    # Criar uma lista para armazenar os valores das células
    valores_celulas = []

    # Iterar sobre as linhas da tabela
    linhas = tabela.find_all('tr')




    for linha in linhas:
        # Encontrar todas as células (colunas) da linha
        celulas = linha.findChildren('td')
        
        
        # Verificar se a linha começa com uma data válida
        if celulas:
            # Obter o texto da primeira célula (que deve conter a data)
            data_texto = celulas[0].get_text(strip=True)
            

            if data_texto > "1999":
                linha = linha.get_text()
                sheet_receita['A1'].value = 'Ano/Mês'
                sheet_receita['B1'].value = 'Jan'
                sheet_receita['C1'].value = 'Fev'
                sheet_receita['D1'].value = 'Mar'
                sheet_receita['E1'].value = 'Abr'
                sheet_receita['F1'].value = 'Mai'
                sheet_receita['G1'].value = 'Jun'
                sheet_receita['H1'].value = 'Jul'
                sheet_receita['I1'].value = 'Ago'
                sheet_receita['J1'].value = 'Set'
                sheet_receita['K1'].value = 'Out'
                sheet_receita['L1'].value = 'Nov'
                sheet_receita['M1'].value = 'Dez'
                sheet_receita['N1'].value = 'Acumulado'

                #valores_linha = [linha.get_text(strip=True) for celula in celulas]
                valores_linha = [celula.get_text(strip=True) for celula in celulas]
                
                for celula in celulas:
                    valor_celula = celula.get_text(strip=True)

                    try:
                        valor_num = float(valor_celula.replace(',', '.'))  # Substituir ',' por '.' para números decimais

                    except ValueError:
                        # Se não for possível converter para float, manter como string
                        valor_num = valor_celula

                if valores_linha:
                    data_texto = valores_linha[0]
                    sheet_receita.append(valores_linha)


# Fechar o navegador
workbook.save('receita.xlsx')

driver.quit()




