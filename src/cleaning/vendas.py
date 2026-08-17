def limpar_vendas(df):
    vendas_suspeitas = df[df['valor_pago'] < 0]
    vendas_validas = df[df['valor_pago'] >= 0]

    vendas_validas = vendas_validas.drop_duplicates(subset=['id_cliente', 'id_servico', 'id_profissional', 'data_venda', 'hora_venda'], keep='first')

    return vendas_validas, vendas_suspeitas