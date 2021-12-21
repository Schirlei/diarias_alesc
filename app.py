import base64
import gspread
import json
import os


spreadsheet_id = os.environ["GOOGLE_SHEET_ID"]
conteudo_codificado = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) #Faz a autenticação
spreadsheet = service_account.open_by_key(spreadsheet_id) #Conecta à planilha
worksheet = spreadsheet.worksheet("Planilha1") #Escolhe a aba
