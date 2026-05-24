from models.produto import Produto

class Suplemento(Produto):
    def __init__(self, nome: str, preco: float, quantidade: int, categoria: str, sabor: str, data_validade: str):
        super().__init__(nome, preco, quantidade, categoria)
        self.sabor = sabor
        self.data_validade = data_validade

    def __str__(self):
        return super().__str__() + f"\n Sabor: {self.sabor}\n Data de validade: {self.data_validade}"
    
    def to_dict(self):
        return super().to_dict() | {"sabor" : self.sabor, "data_validade" : self.data_validade}