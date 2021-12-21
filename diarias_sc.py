import pandas as pd
from datetime import datetime, timedelta
def raspar_alesc_escrever_spreadsheet(worksheet):
    df = pd.read_csv('https://transparencia.alesc.sc.gov.br/diarias_csv.php?ano=2021',
                     sep=';',
                     encoding='iso 8859-1')
    dados = df.to_dict('records')
    ontem = datetime.today() - timedelta(days=1)
    for dado in dados:
        data = datetime.strptime(dado['Data'], '%d/%m/%Y')
        #se a data for maior do que ontem, acrescentar à planilha
        if data > ontem:
            #acresentar à planilha
            worksheet.append_row(list(dado.values()))
