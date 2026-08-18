# Barbearia Alpha — Pipeline de Engenharia de Dados

Projeto de portfólio que simula, de ponta a ponta, o trabalho de um Engenheiro de Dados Jr: gerar dados fictícios (incluindo problemas reais de qualidade, como duplicatas e inconsistências de formato), tratá-los com Python, carregá-los em um banco relacional e disponibilizá-los em um dashboard interativo.

## Objetivo

A "Barbearia Alpha" é uma empresa fictícia que possui dados de clientes, profissionais, serviços e vendas espalhados em planilhas Excel — um cenário comum em pequenos negócios reais. O projeto constrói um pipeline completo para:

- Simular dados realistas, incluindo erros humanos comuns (duplicatas, telefones em formatos inconsistentes, valores inválidos);
- Limpar e validar esses dados de forma automatizada e reprocessável;
- Armazená-los em um banco relacional (PostgreSQL), com carga idempotente;
- Disponibilizar métricas de negócio em um dashboard interativo (Power BI).

Este projeto também serve como demonstração prática para oferecer serviços de organização e automação de dados para pequenas empresas.

## Arquitetura

```text
Excel (dados fictícios)
        │
        ▼
   Python (Faker)
        │
        ▼
data/raw/  ──────────────►  data_dirtying/ (sujeira simulada, opcional)
        │
        ▼
   Limpeza e Validação (pandas)
        │
        ▼
data/processed/
        │
        ▼
   PostgreSQL (carga idempotente)
        │
        ▼
      Power BI
```

## Tecnologias

- **Python** — geração, limpeza e carga de dados
- **Faker** — geração de dados fictícios realistas (pt_BR)
- **pandas** — limpeza, transformação e padronização
- **PostgreSQL** — armazenamento relacional
- **psycopg2** — conexão e carga no banco
- **python-dotenv** — gerenciamento seguro de credenciais
- **Power BI** — visualização e dashboard

## Estrutura do projeto

```text
barbearia-alpha/
├── assets/
|
├── data/
│   ├── raw/              # dados "como chegaram" (não versionado)
│   └── processed/        # dados após limpeza (não versionado)
├── powerbi/
│   └── barbearia_alpha.pbix
├── src/
│   ├── generators/       # geração de dados fictícios (Faker)
│   ├── data_dirtying/    # simulação de problemas reais de dados
│   ├── cleaning/         # limpeza e padronização (pandas)
│   ├── exporters/        # exportação para Excel
│   ├── database/         # schema, conexão e carga no PostgreSQL
│   ├── main.py           # orquestra a geração dos dados
│   └── limpar.py         # orquestra a limpeza dos dados
├── .env                  # credenciais (não versionado)
├── .gitignore
└── requirements.txt
```

## Instalação

```bash
git clone <url-do-repositorio>
cd barbearia-alpha
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto com suas credenciais do PostgreSQL:

```env
DB_HOST=localhost
DB_NAME=barbearia_alpha
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_PORT=5432
```

Crie o banco de dados e rode o schema (`src/database/schema.sql`) no seu PostgreSQL local.

## Execução

```bash
python src/main.py               # gera os dados fictícios em data/raw/
python src/limpar.py             # limpa e valida, salva em data/processed/
python src/database/carregar.py  # carrega os dados no PostgreSQL
```

Abra `powerbi/barbearia_alpha.pbix` no Power BI Desktop para visualizar o dashboard (conectado ao seu PostgreSQL local).

## Decisões técnicas em destaque

- **Dados sujos simulados de propósito** — em vez de usar um dataset genérico de terceiros, o próprio pipeline injeta problemas realistas (duplicatas, telefones com formatos inconsistentes, valores negativos) para testar de verdade a lógica de limpeza.
- **Separação raw / processed** — os dados originais nunca são sobrescritos, permitindo reprocessar a limpeza quantas vezes forem necessárias sem perder o dado de origem.
- **Carga idempotente** — a carga no PostgreSQL usa `INSERT ... ON CONFLICT DO NOTHING`, permitindo rodar o pipeline múltiplas vezes sem duplicar dados.
- **Separação entre confiabilidade e formato** — vendas com valores negativos são isoladas para revisão manual, em vez de corrigidas automaticamente, evitando mascarar erros mais graves.

## Resultados

![Dashboard Barbearia Alpha](assets/image.png)

- 50 clientes, 5 profissionais, 4 serviços, ~170 vendas válidas processadas
- Faturamento total: ~R$ 7.740 | Ticket médio: ~R$ 45,53
- Pipeline testado com carga dupla, confirmando idempotência

## Próximos passos

- Containerizar o pipeline com Docker
- Orquestrar as etapas com Airflow
- Publicar o dashboard no Power BI Service para acesso remoto
