import pandas as pd
from conexao import conectar
from pathlib import Path


RAIZ_PROJETO = Path(__file__).parent.parent.parent
PASTA_DATA_RAW = RAIZ_PROJETO / "data" / "raw"
PASTA_DATA_PROCESSED = RAIZ_PROJETO / "data" / "processed"

profissional = pd.read_excel(PASTA_DATA_PROCESSED / "profissionais_limpos.xlsx")
servicos = pd.read_excel(PASTA_DATA_RAW / "servicos.xlsx")
clientes = pd.read_excel(PASTA_DATA_PROCESSED / "clientes_limpos.xlsx")
vendas = pd.read_excel(PASTA_DATA_PROCESSED / "vendas_limpas.xlsx")


def carregar_clientes(df, conexao):
    cursor = conexao.cursor()

    sql = """
    INSERT INTO clientes (id_cliente, nome, telefone)
    VALUES (%s, %s, %s)
    ON CONFLICT (id_cliente) DO NOTHING;
    """

    for i in range(len(df)):
        linha = df.iloc[i]
        valores = (int(linha['id_cliente']), linha['nome'], linha['telefone'])
        cursor.execute(sql, valores)

    conexao.commit()


def carregar_profissionais(df, conexao):
    cursor = conexao.cursor()

    sql = """
    INSERT INTO profissional (id_profissional, nome, telefone)
    VALUES (%s, %s, %s)
    ON CONFLICT (id_profissional) DO NOTHING;
    """

    for i in range(len(df)):
        linha = df.iloc[i]
        valores = (int(linha['id_profissional']), linha['nome'], linha['telefone'])
        cursor.execute(sql, valores)

    conexao.commit()


def carregar_servicos(df, conexao):
    cursor = conexao.cursor()

    sql = """
    INSERT INTO servicos (id_servico, tipo_servico, preco, tempo_estimado)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (id_servico) DO NOTHING;
    """

    for i in range(len(df)):
        linha = df.iloc[i]
        valores = (int(linha['id_servico']), linha['tipo_servico'], float(linha['preco']), int(linha['tempo_estimado']))
        cursor.execute(sql, valores)

    conexao.commit()


def carregar_vendas(df, conexao):
    cursor = conexao.cursor()

    sql = """
    INSERT INTO vendas (id_venda, id_servico, id_cliente, id_profissional, data_venda, hora_venda, valor_pago)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id_venda) DO NOTHING;
    """

    for i in range(len(df)):
        linha = df.iloc[i]
        valores = (int(linha['id_venda']), int(linha['id_servico']), int(linha['id_cliente']), int(linha['id_profissional']), linha['data_venda'], linha['hora_venda'], float(linha['valor_pago']))
        cursor.execute(sql, valores)

    conexao.commit()


conexao = conectar()

carregar_profissionais(profissional, conexao)
carregar_servicos(servicos, conexao)
carregar_clientes(clientes, conexao)
carregar_vendas(vendas, conexao)

conexao.close()