import random

class Produto: 
    codigos_usados = [] 

    def __init__(self, nome: str, preco: float, quantidade: int, categoria: str):
        self.nome = nome 
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria
        self.codigo = self.gerar_codigo()

    def gerar_codigo(self):
        while True:
            codigo = random.randint(1000, 9999)
            if codigo not in Produto.codigos_usados:
                Produto.codigos_usados.append(codigo)
                return codigo
    
    def __str__(self):
        return f" Nome: {self.nome}\n Preço: {self.preco}\n Quantidade: {self.quantidade}\n Categoria: {self.categoria}\n Codigo: {self.codigo}"
    
    def to_dict(self):
        return{
            "nome" : self.nome,
            "preco" : self.preco,
            "quantidade" : self.quantidade, 
            "categoria" : self.categoria, 
            "codigo" : self.codigo
        }