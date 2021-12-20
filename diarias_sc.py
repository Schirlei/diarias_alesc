import csv
import datetime
import io
import requests
import pandas as pd

url = "https://transparencia.alesc.sc.gov.br/diarias_dados_abertos.php"
resposta = requests.get(url)
html = resposta.text 
print(html)

partes = html.split('<td style = "text-align: center"><a href="')
partes[-1]

for parte in partes:     ### itera em cima da lista de trechos de código.
    subpartes = parte.split('</a></td>')   #padrão usado para quebrar em subpartes.
    conteudo = subpartes[0]  ### seleciona a primeira parte antes do padrão utilizado anteriormente.
    print(subpartes)

for parte in partes:
    conteudo = subpartes[0]
    subpartes = parte.split('" class="btn btn-download">Download')
    if 'diarias_csv.php' not in conteudo:
       continue
    print(conteudo)

arquivo = open("links-diarias.csv", mode="w") 
escritor = csv.DictWriter(arquivo, fieldnames=["ano", "link"]) 
escritor.writeheader()
for parte in partes:   
    subpartes = parte.split('" class="btn btn-download">Download')  
    conteudo = subpartes[0]  
    if 'diarias_csv.php' not in conteudo:  
      continue  ### pula para a próxima iteração do 'for'.
    lista = conteudo.split('diarias_csv.php?ano=')   
    ano = lista[1]
    link = f'https://transparencia.alesc.sc.gov.br/{conteudo}'
    escritor.writerow({"ano": ano, "link": link})   
arquivo.close()
  
def extrai_links(html):   
    links = []
    partes = html.split('<td style = "text-align: center"><a href="')
    for parte in partes:   
        subpartes = parte.split('" class="btn btn-download">Download')  
        conteudo = subpartes[0]
      if 'diarias_csv.php' not in conteudo: 
         continue  
      lista = conteudo.split('diarias_csv.php?ano=')  
      ano = lista[1]
      link = f'https://transparencia.alesc.sc.gov.br/{conteudo}'
      links.append({"ano": ano, "link": link})    ## retorna uma lista.
    return links 
  
url = "https://transparencia.alesc.sc.gov.br/diarias_dados_abertos.php"
resposta = requests.get(url)
html = resposta.text
arquivo = open("links-diarias-2.csv", mode="w")  
escritor = csv.DictWriter(arquivo, fieldnames=["ano", "link"]) 
escritor.writeheader()
for link_diaria in extrai_links(html):
    escritor.writerow(link_diaria)
arquivo.close()

df = pd.read_csv('links-diarias.csv')  
links = list(df['link'])    
links

print('Iniciando o dataframe com ', links[0]) 
    
df = pd.read_csv(links[0], encoding='iso8859-1', sep=';')   

for url in links[1:]:   ### Aqui o 'for' abre os outros links. 
    print('Acrescentando ', url)
    df2 = pd.read_csv(url, encoding='iso8859-1', sep=';') 
    df = pd.concat([df, df2]) 
    
df['Ano'] = df['Data'].str.split('/').str[-1]

df.to_csv('diarias_final.csv')
