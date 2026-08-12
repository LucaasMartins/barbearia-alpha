servicos = {
    'Corte Social': {
        'preco': 30.00,
        'tempo_estimado': 30,
    },
    'Corte Degradê': {
        'preco': 40.00,
        'tempo_estimado': 45,
    },
    'Corte + Barba': {
        'preco': 50.00,
        'tempo_estimado': 60,
    },
    'Corte + Barba + Sobrancelha': {
        'preco': 60.00,
        'tempo_estimado': 75,
    },
}


def gerar_servico():

    servico = []

    for id_servico, (tipo_servico, detalhes) in enumerate(servicos.items()):
        servico.append({
            'id_servico': id_servico,
            'tipo_servico': tipo_servico,
            'preco': detalhes['preco'],
            'tempo_estimado': detalhes['tempo_estimado'],
        })
    return servico