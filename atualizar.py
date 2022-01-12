import base64
import json
import os
import gspread
import pandas as pd
from datetime import datetime, timedelta


spreadsheet_id = os.environ["GOOGLE_SHEET_ID"]
conteudo_codificado = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) #Faz a autenticação
spreadsheet = service_account.open_by_key(spreadsheet_id) #Conecta à planilha
worksheet = spreadsheet.worksheet("Página1") #Escolhe a aba

def raspar_alesc_escrever_spreadsheet(worksheet):
    df = pd.read_csv('https://transparencia.alesc.sc.gov.br/diarias_csv.php?ano=2021',
                     sep=';',
                     encoding='iso 8859-1')
    dados = df.to_dict('records')
    #ontem = datetime.today() - timedelta(days=1)
    for dado in dados:
        exists = worksheet.findall(dado['Relatório'])
        if not exists:
            worksheet.append_row(list(dado.values()))
                                 
        #data = datetime.strptime(dado['Data'], '%d/%m/%Y')
        #se a data for maior do que ontem, acrescentar à planilha
        #if data > ontem:
            #worksheet.append_row(list(dado.values()))
            
#torna .py "executável"
if __name__ == '__main__':
    raspar_alesc_escrever_spreadsheet(worksheet)
