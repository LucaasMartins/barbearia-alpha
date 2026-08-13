import random

PORCENTAGEM_DUPLICATAS = 0.10
PORCENTAGEM_VALORES_NEGATIVOS = 0.15

def sujar_vendas(vendas):
    vendas_sujas = [vendas.copy() for venda in vendas]

    quantidade_negativos = round(len(vendas) * PORCENTAGEM_VALORES_NEGATIVOS)
    vendas_para_negativar = random.sample(vendas_sujas, quantidade_negativos)

    for venda in vendas_para_negativar:
        venda['valor_pago'] = venda['valor_pago'] * -1

    quantidade_duplicatas = round(len(vendas) * PORCENTAGEM_DUPLICATAS)
    vendas_para_duplicar = random.sample(vendas_sujas, quantidade_duplicatas)

    for venda in vendas_para_duplicar:
        venda_duplicada = venda.copy()

        vendas_sujas.append(venda_duplicada)

    return vendas_sujas