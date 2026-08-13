import random

PORCENTAGEM_DUPLICATAS = 0.10

def sujar_clientes(clientes):
    clientes_sujos = clientes.copy()

    quantidade_duplicatas = round(len(clientes) * PORCENTAGEM_DUPLICATAS)
    clientes_para_duplicar = random.sample(clientes_sujos, quantidade_duplicatas)

    for cliente in clientes_para_duplicar:
        cliente_duplicado = cliente.copy()

        # simula inconsistência: telefone sem formatação (só dígitos)
        cliente_duplicado['telefone'] = cliente_duplicado['telefone'].replace(' ', '').replace('-', '').replace('(', '').replace(')', '')

        # simula inconsistência: nome com espaços extras (erro comum de digitação)
        cliente_duplicado['nome'] = f"  {cliente_duplicado['nome']}  "

        clientes_sujos.append(cliente_duplicado)

    return clientes_sujos