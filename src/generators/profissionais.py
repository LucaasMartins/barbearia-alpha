from faker import Faker

def gerar_profissionais(quantidade):
    fake = Faker('pt_BR')
    profissionais = []

    for id_profissional in range(quantidade):
        profissional = {
            'id_profissional': id_profissional,
            'nome': fake.name(),
            'telefone': fake.phone_number(),
        }

        profissionais.append(profissional)

    return profissionais