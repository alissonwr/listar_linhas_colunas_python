import pandas as pd

def listar_linhas(excel_path):
    # Carregar a planilha de origem
    df = pd.read_excel(excel_path)
    
    # Listar as linhas com seus índices
    for idx, row in df.iterrows():
        print(f"Índice: {idx}, Linha: {row.tolist()}")

# Exemplo de uso
listar_linhas('teste.xlsx')
