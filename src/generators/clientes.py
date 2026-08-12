from faker import Faker

def gerar_clientes(quantidade):
    fake = Faker('pt_BR')
    clientes = []

    for id_cliente in range(quantidade):
        cliente = {
            'id_cliente': id_cliente,
            'nome': fake.name(),
            'telefone': fake.phone_number(),
        }

        clientes.append(cliente)

    return clientes