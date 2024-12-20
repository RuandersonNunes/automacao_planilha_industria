from functions import *
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

filename = 'crypto-reality-445301-c5-c999996299cb.json'

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = Credentials.from_service_account_file(
    filename=filename,
    scopes=scopes
)

client = gspread.authorize(creds)

planilha_completa = client.open(
    "planilha_industria"
)

planilha = planilha_completa.get_worksheet(1)

mostrar_planilha(planilha)