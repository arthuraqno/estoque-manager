from models.produto import Produto

class Equipamento(Produto):
    def __init__(self, nome: str, preco: float, quantidade: int, categoria: str, tamanho: str):
        super().__init__(nome, preco, quantidade, categoria)
        self.tamanho = tamanho

    def __str__(self):
        return super().__str__() + f"\n Tamanho: {self.tamanho}"

    def to_dict(self):
        return super().to_dict() | {"tamanho" : self.tamanho}