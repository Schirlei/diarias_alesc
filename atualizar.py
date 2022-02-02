import base64
import json
import os
import gspread
import pandas as pd
import time
from datetime import datetime, timedelta


spreadsheet_id = os.environ["GOOGLE_SHEET_ID"]
conteudo_codificado = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) #Faz a autenticação
spreadsheet = service_account.open_by_key(spreadsheet_id) #Conecta à planilha
worksheet = spreadsheet.worksheet("Página1") #Escolhe a aba
valores_atuais = worksheet.col_values(7)

def raspar_alesc_escrever_spreadsheet(worksheet):
    df = pd.read_csv('https://transparencia.alesc.sc.gov.br/diarias_csv.php?ano=2011',
                     sep=';',
                     encoding='iso 8859-1')
    dados = df.to_dict('records')
    print(f"Processando {len(dados)} linhas…")
    for dado in dados:
        exists = dado['Relatório'] in valores_atuais
        if not exists:
            worksheet.append_row(list(dado.values()))
            time.sleep(1.25)
        else:  
            print(f"Relatório {dado['Relatório']} já existe")
                                   
            
#torna .py "executável"
if __name__ == '__main__':
    raspar_alesc_escrever_spreadsheet(worksheet)
