import pandas as pd

def salvar_como_excel(dados, caminho):
    
    df = pd.DataFrame(dados)

    df.to_excel(caminho, index=False)