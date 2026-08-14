import re

def padronizar_telefone(telefone):
    apenas_digitos = re.sub(r'\D', '', telefone)

    if len(apenas_digitos) > 11:
        apenas_digitos = apenas_digitos[2:]

    ddd = apenas_digitos[0:2]
    primeira_metade = apenas_digitos[2:7]
    segunda_metade = apenas_digitos[7:]

    return f"({ddd}) {primeira_metade}-{segunda_metade}"

def limpar_clientes():
    pass