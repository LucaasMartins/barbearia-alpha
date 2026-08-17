from cleaning.utils import padronizar_telefone

def limpar_profissionais(df):
    df['telefone'] = df['telefone'].apply(padronizar_telefone)
    df['nome'] = df['nome'].str.strip()
    return df