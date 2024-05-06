import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import openpyxl  
import pandas as pd






# Abrir o navegador
driver = webdriver.Chrome()
driver.get('https://investidor10.com.br/indices/cdi/')

# Obter o código fonte da página após o carregamento completo
req = driver.page_source

# Utilizar BeautifulSoup para analisar o código HTML
soup = BeautifulSoup(req, 'html.parser')

# Encontrar a tabela desejada com base na classe
tabela = soup.find('table', attrs={"class": "table table-bordered table-striped"})

# Criar um novo arquivo Excel
workbook = openpyxl.Workbook()
sheet_receita = workbook.active
sheet_receita.title = 'receita'

# Verificar se a tabela foi encontrada
if tabela:
    # Iterar sobre as linhas da tabela
    linhas = tabela.find_all('tr')

    # Definir cabeçalho da planilha
    cabecalho = ['Ano/Mês', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Acumulado']
    sheet_receita.append(cabecalho)

    for linha in linhas:
        # Encontrar todas as células (colunas) da linha
        celulas = linha.find_all('td')
        
        # Verificar se há células na linha
        if celulas:
            # Obter o texto da primeira célula (que deve conter a data)
            data_texto = celulas[0].get_text(strip=True)
            
            # Verificar se a linha começa com uma data válida (ano maior que 1999)
            if data_texto > '1999':
                # Obter os valores das células como números (se possível)
                valores_linha = []
                
                for celula in celulas:
                    # Obter o texto da célula
                    valor_celula = celula.get_text(strip=True)
                    
                    # Converter o valor para número (se possível)
                    try:
                        valor_num = float(valor_celula.replace(',', '.'))  # Substituir ',' por '.' para números decimais
                    except ValueError:
                        # Se não for possível converter para float, atribuir None
                        valor_num = None
                    
                    # Adicionar o valor à lista de valores da linha

                    
                    valores_linha.append(valor_num)
                
                # Adicionar os valores à planilha
                sheet_receita.append(valores_linha)

# Salvar o arquivo Excel
workbook.save('receita.xlsx')

# Fechar o navegador
driver.quit()

################################################################################################################

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

################################################################################################################

def contarLinhas(nomeTbaela):
     df = pd.read_excel(nomeTbaela)
     numLinhas = len(df)
     return numLinhas + 1


qtdLinhasPlanilha = contarLinhas(arquivo)

def criaArquivo(nomePlan, numeroLinhas, media):
    
        with open('relatorio.txt', 'w') as relatorio:
            relatorio.write(f'Nome da planilha: {nomePlan}\n')
            relatorio.write(f'Número total de linhas: {numeroLinhas}\n')
            relatorio.write(f'Média: {media}\n')
    
    
      

criaArquivo(nomePlanilha, qtdLinhasPlanilha, mediaCdi)

