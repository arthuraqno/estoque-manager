from models.produto import Produto
from datetime import date 

class Venda:
    def __init__(self, produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_total = produto.preco * quantidade
        self.data_venda = date.today()

    def __str__(self):
        return f"VENDA REALIZADA EM {self.data_venda}\n Produto: {self.produto}\n Quantidade {self.quantidade}\n Preço total: {self.preco_total}"
    
    def to_dict(self):
        return {
            "produto" : self.produto.nome, 
            "quantidade" : self.quantidade,
            "preco_total" : self.preco_total, 
            "data_venda" : str(self.data_venda)
        }