from selenium import webdriver
from selenium.webdriver.common.by import By 
import openpyxl  

#acessar site https://www.pichau.com.br/hardware/placa-m-e

driver = webdriver.Chrome()
driver.get('https://www.cacaushow.com.br/categoria/biscoito')

#extrair todos os titulos



titulos = driver.find_elements(By.XPATH, "//div[@class='pdp-link product-name-cap']")


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


def calcularValores(arquivoExcel, coluna, linhas):

    df=pd.read_excel(arquivoExcel)

    if coluna not in df.columns:
        print('coluna n encontrada')
        return
    
    tot = 0

    for linha in linhas:

        if linha >= len(df):
            print(f"A linha {linha} está fora do intervalo do arquivo Excel.")
            continue

    valor_celula = df.loc[linha, coluna]

    if pd.notna(valor_celula) and pd.api.types.is_numeric_dtype(df[coluna].dtype):
        tot += valor_celula
        

    return tot / coluna

arquivo = 'receita.xlsx' 
colunaCalculo = 'N'
linhasEscolhidas = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

mediaCdi = calcularValores(arquivo, colunaCalculo, linhasEscolhidas)
print(mediaCdi)