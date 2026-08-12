from generators.clientes import gerar_clientes
from generators.profissionais import gerar_profissionais
from generators.servicos import gerar_servico
from generators.vendas import gerar_vendas
import pandas as pd
from exporters.excel import salvar_como_excel


QTD_CLIENTES = 50
QTD_PROFISSIONAIS = 5
QTD_VENDAS = 200

clientes = gerar_clientes(QTD_CLIENTES)
profissionais = gerar_profissionais(QTD_PROFISSIONAIS)
servicos = gerar_servico()
vendas = gerar_vendas(QTD_VENDAS, clientes, profissionais, servicos)

salvar_como_excel(clientes, '../data/raw/clientes.xlsx')
salvar_como_excel(profissionais, '../data/raw/profissionais.xlsx')
salvar_como_excel(servicos, '../data/raw/servicos.xlsx')
salvar_como_excel(vendas, '../data/raw/vendas.xlsx')