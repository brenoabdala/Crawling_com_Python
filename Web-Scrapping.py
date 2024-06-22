# Bibliotecas instalação
# pip install requests
# pip install bs4
# pip install pandas

# Importando biblioteca
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_valores = []

#Requisições
response_dolar = requests.get('https://dolarhoje.com/')
response_real = requests.get('https://www.binance.com/pt/price/bitcoin/BRL')

content_dolar = response_dolar.content
content_real = response_real.content

# Conversão para HTML
site_dolar = BeautifulSoup(content_dolar, 'html.parser')
site_real = BeautifulSoup(content_real, 'html.parser')

# HTML dos valores
vl_dolar = site_dolar.find('input', id='nacional')['value']
vl_real = site_real.findAll('div', attrs={'class': 'css-1bwgsh3'})

lista_valores.append(vl_dolar)

for real in vl_real:
    # print(real.get_text())
    lista_valores.append(real.get_text())

#Tratamentos dos dados
df = pd.DataFrame(data = [lista_valores], columns=['Valor_do_Dolar', 'Biticon_em_reais'])
df['Biticon_em_reais'] = df['Biticon_em_reais'].str.replace('R$', '')
df['Biticon_em_reais'] = df['Biticon_em_reais'].str.replace(',', '').astype(float)

df['Valor_do_Dolar'] = df['Valor_do_Dolar'].str.replace(',', '.').astype(float)


biticon = df['Biticon_em_reais'][0]
dolar = df['Valor_do_Dolar'][0]

#bitcoin em reais / dolar em reais = bitcoin em dólares

conversao = biticon / dolar

print(f'Breno_Rossi_Abdala >> 1 bitcoin (R$ {biticon}) vale US$ {conversao:,.2f} (US$1 = R$ {dolar})')

