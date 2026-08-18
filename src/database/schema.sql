DROP TABLE IF EXISTS vendas;
DROP TABLE IF EXISTS servicos;
DROP TABLE IF EXISTS profissional;
DROP TABLE IF EXISTS clientes;


CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome TEXT,
    telefone VARCHAR(15)
);

CREATE TABLE profissional (
    id_profissional INTEGER PRIMARY KEY,
    nome TEXT,
    telefone VARCHAR(15)
);

CREATE TABLE servicos (
    id_servico INTEGER PRIMARY KEY,
    tipo_servico TEXT,
    preco NUMERIC(10, 2),
    tempo_estimado INTEGER
);

CREATE TABLE vendas (
    id_venda INTEGER PRIMARY KEY,
    id_servico INTEGER REFERENCES servicos(id_servico),
    id_cliente INTEGER REFERENCES clientes(id_cliente),
    id_profissional INTEGER REFERENCES profissional(id_profissional),
    data_venda DATE,
    hora_venda TIME,
    valor_pago NUMERIC(10, 2)
);