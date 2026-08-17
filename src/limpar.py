import pandas as pd
from pathlib import Path
from cleaning.clientes import limpar_clientes
from cleaning.profissionais import limpar_profissionais
from cleaning.vendas import limpar_vendas
from exporters.excel import salvar_como_excel

RAIZ_PROJETO = Path(__file__).parent.parent

PASTA_DATA_RAW = RAIZ_PROJETO / "data" / "raw"
PASTA_DATA_PROCESSED = RAIZ_PROJETO / "data" / "processed"
PASTA_DATA_PROCESSED.mkdir(parents=True, exist_ok=True)

clientes = pd.read_excel(PASTA_DATA_RAW / 'clientes.xlsx')
profissional = pd.read_excel(PASTA_DATA_RAW / 'profissionais.xlsx')
vendas = pd.read_excel(PASTA_DATA_RAW / 'vendas.xlsx')

clientes_limpos = limpar_clientes(clientes)
profissionais_limpos = limpar_profissionais(profissional)
vendas_limpas, vendas_suspeitas = limpar_vendas(vendas)

salvar_como_excel(clientes_limpos, PASTA_DATA_PROCESSED / 'clientes_limpos.xlsx')
salvar_como_excel(profissionais_limpos, PASTA_DATA_PROCESSED / 'profissionais_limpos.xlsx')
salvar_como_excel(vendas_limpas, PASTA_DATA_PROCESSED / 'vendas_limpas.xlsx')
salvar_como_excel(vendas_suspeitas, PASTA_DATA_PROCESSED / 'vendas_suspeitas.xlsx')

print(f"clientes: {len(clientes)} -> {len(clientes_limpos)} limpos")
print(f"profissionais: {len(profissional)} -> {len(profissionais_limpos)} limpos")
print(f"vendas: {len(vendas)} -> {len(vendas_limpas)} válidas, {len(vendas_suspeitas)} suspeitas")