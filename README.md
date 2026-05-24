# 📦 Estoque Manager

Sistema de gerenciamento de estoque para loja de Jiu-Jitsu, desenvolvido em Python.

## 📋 Funcionalidades

- Cadastrar equipamentos (kimonos, rashguards, faixas) e suplementos
- Realizar vendas com baixa automática no estoque
- Repor estoque de produtos
- Deletar produtos
- Listar produtos e histórico de vendas
- Dados persistidos em JSON

## 📁 Estrutura do Projeto
estoque-manager/
├── main.py
├── models/
│   ├── produto.py
│   ├── equipamento.py
│   ├── suplemento.py
│   └── venda.py
├── services/
│   └── estoque.py
└── data/
├── produtos.json
└── vendas.json

## ▶️ Como rodar

```bash
cd estoque-manager
python main.py
```

## 🛠️ Tecnologias

- Python 3.14
- JSON para persistência de dados
- Orientação a objetos com herança

## 📚 Conceitos aplicados

- Herança e classes abstratas
- Encapsulamento
- Type hints
- Persistência de dados com JSON
- Menus interativos no terminal