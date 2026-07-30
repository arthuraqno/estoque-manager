# 📦 Estoque Manager

Sistema de gerenciamento de estoque para loja de Jiu-Jitsu, desenvolvido em Python.

## 📋 Funcionalidades

- Cadastrar equipamentos (kimonos, rashguards, faixas) e suplementos
- Realizar vendas com baixa automática no estoque
- Repor estoque de produtos
- Deletar produtos
- Listar produtos e histórico de vendas
- Dados persistidos em banco de dados PostgreSQL

## 📁 Estrutura do Projeto

estoque-manager/
├── main.py
├── base.py
├── database.py
├── models/
│ ├── produto.py
│ ├── equipamento.py
│ ├── suplemento.py
│ └── venda.py
└── services/
└── estoque.py


## ▶️ Como rodar

1. Crie um banco de dados PostgreSQL chamado `estoque_db`
2. Configure a conexão em `database.py` com seu usuário e senha
3. Execute `python database.py` para criar as tabelas
4. Execute `python main.py` para iniciar o sistema

## 🛠️ Tecnologias

- Python 3.14
- PostgreSQL
- SQLAlchemy (ORM)
- psycopg2

## 📚 Conceitos aplicados

- Herança e polimorfismo com SQLAlchemy
- Mapeamento objeto-relacional (ORM)
- Banco de dados relacional com PostgreSQL
- Menus interativos no terminal