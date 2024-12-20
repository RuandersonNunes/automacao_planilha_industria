import pandas as pd

def mostrar_planilha(planilha):
    dados = planilha.get_all_records()
    df = pd.DataFrame(dados)
    print(df)