from faker import Faker
import random
from datetime import date

def gerar_vendas(quantidade, clientes, profissionais, servicos):
    faker = Faker('pt_BR')
    vendas = []

    for id_venda in range(quantidade):

        servico_sorteado = random.choice(servicos)

        venda = {
            'id_venda': id_venda,
            'id_cliente': random.choice(clientes)['id_cliente'],
            'id_profissional': random.choice(profissionais)['id_profissional'],
            'id_servico': servico_sorteado['id_servico'],
            'valor_pago': servico_sorteado['preco'],
            'data_venda': faker.date_between(start_date=date(2026, 7, 1), end_date=date(2026, 7, 31)),
            'hora_venda': f"{random.randint(9, 19):02d}:{random.randint(0, 59):02d}"
        }
        vendas.append(venda)

    return vendas