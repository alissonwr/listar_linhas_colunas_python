import pandas as pd

def listar_colunas(excel_path):
    # Carregar a planilha de origem
    df = pd.read_excel(excel_path)
    
    # Listar as colunas com seus índices
    colunas = df.columns
    for idx, col in enumerate(colunas):
        print(f"Índice: {idx}, Coluna: {col}")

# Exemplo de uso
listar_colunas('Operacional_Água_RESPONSAVEIS.xlsx')
