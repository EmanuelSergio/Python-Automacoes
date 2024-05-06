from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import openpyxl  



driver = webdriver.Chrome()
driver.get('https://investidor10.com.br/indices/cdi/')
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
tabela = soup.find('table', attrs={"class":"table table-bordered table-striped"})

contador = 0



if tabela:
    # Criar uma lista para armazenar os valores das células
    valores_celulas = []

    # Iterar sobre as linhas da tabela
    linhas = tabela.find_all('tr')
    for linha in linhas:
        # Encontrar todas as células (colunas) da linha
        celulas = linha.find_all('td')
        for celula in celulas:
            # Obter o texto da célula e adicionar à lista de valores
            valor_celula = celula.get_text(strip=True)
            valores_celulas.append(valor_celula)

    # Imprimir os valores das células
    for valor in valores_celulas:
        print(valor) 

        

#extrair todos os titulos


"""

#extrair preços antigos
precosAntigo = driver.find_elements(By.XPATH,"//span[@class='strike-through list']")

#extrair preços novos
precos = driver.find_elements(By.XPATH,"//div[@class='it__shelf__discountPrice']")

#criando a planilha
workbook = openpyxl.Workbook()
#criando a pagina produtos
workbook.create_sheet('produtos')
#seleciono a pagina produtos
sheet_produtos = workbook['produtos']

sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço antigo'
sheet_produtos['C1'].value = 'Preço atual'

print("Número de títulos:", len(titulos))
print("Preço antigo:", len(precosAntigo))
print("Preço atual:", len(precos))


#inserir na planilha
for titulo, precoAntigo, preco in zip(titulos, precosAntigo, precos):
    print('nome: ', titulo.text)
    print('valor anterior: ',precoAntigo.text)
    print('valor atual: ', preco.text)
    sheet_produtos.append([titulo.text,precoAntigo.text, preco.text])
    
    

workbook.save('produtos.xlsx')


"""