from models.equipamento import Equipamento
from models.produto import Produto
from models.suplemento import Suplemento
from models.venda import Venda
import json

class Estoque: 
    def __init__(self):
        self.produtos = []
        self.vendas = []

    def cadastrar_equipamento(self, equipamento: Equipamento):
        self.produtos.append(equipamento)
        print (f"{equipamento.nome} adcionado ao estoque")

    def cadastrar_suplemento(self, suplemento: Suplemento):
        self.produtos.append(suplemento)
        print (f"{suplemento.nome} adcionado ao estoque")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrato!")
            return
        for produtos in self.produtos:
            print(f"Produtos disponíveis:\n{produtos}")

    def realizar_venda(self, produto, quantidade: int):
        if produto not in self.produtos:
            print("O produto não está disponível!")
            return
        elif produto.quantidade < quantidade:
            print("Não ha quantidade disponível para venda")
        else:
            venda = Venda(produto, quantidade)
            produto.quantidade -= quantidade
            self.vendas.append(venda)
            print(f"Venda realizada com sucesso! Total: R${venda.preco_total}")

    def listar_vendas(self):
        if not self.vendas:
            print("Nenhuma venda foi realizada!")
            return
        for vendas in self.vendas:
            print(vendas)

    def repor_estoque(self, produto, quantidade: int):
        produto.quantidade += quantidade
        print(f"Estoque reposto! {produto.nome} agora tem {produto.quantidade} unidades")

    def buscar_produto(self, nome: str):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto
        return None
    
    def deletar_produto(self, produto):
        self.produtos.remove(produto)
        print(f"✅ {produto.nome} removido do estoque!")
    
    def salvar_dados(self):
        with open("data/vendas.json", "w") as f:
            json.dump([venda.to_dict() for venda in self.vendas], f, indent=4)

        with open("data/produtos.json", "w") as f:
            json.dump([produto.to_dict() for produto in self.produtos], f, indent=4)

    def carregar_dados(self):
        try:
            with open("data/produtos.json", "r") as f:
                produtos = json.load(f)
                for p in produtos:
                    if p["categoria"] == "equipamento":
                        produto = Equipamento(p["nome"], p["preco"], p["quantidade"], p["categoria"], p["tamanho"])
                    else:
                        produto = Suplemento(p["nome"], p["preco"], p["quantidade"], p["categoria"], p["sabor"], p["data_validade"])
                    produto.codigo = p["codigo"]
                    Produto.codigos_usados.append(p["codigo"])
                    self.produtos.append(produto)
        except (FileNotFoundError, ValueError):
            pass

        try:
            with open("data/vendas.json", "r") as f:
                vendas = json.load(f)
                for v in vendas:
                    produto = self.buscar_produto(v["produto"])
                    if produto:
                        venda = Venda(produto, v["quantidade"])
                        self.vendas.append(venda)
        except (FileNotFoundError, ValueError):
            pass
