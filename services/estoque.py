from sqlalchemy.orm import Session
from models.equipamento import Equipamento
from models.suplemento import Suplemento
from models.venda import Venda
from models.produto import Produto
from database import engine

class Estoque:
    def cadastrar_equipamento(self, nome, preco, quantidade, categoria, tamanho):
        with Session(engine) as session:
            equipamento = Equipamento(nome = nome, 
                                      preco = preco,
                                      quantidade = quantidade,
                                      categoria = categoria, 
                                      tamanho = tamanho)
            session.add(equipamento)
            session.commit()
            print(f"{nome} adcionado ao estoque") 

    def cadastrar_suplemento(self, nome, preco, quantidade, categoria, sabor, data_validade):
        with Session(engine) as session:
            suplemento = Suplemento(nome = nome, 
                                    preco = preco,
                                    quantidade = quantidade,
                                    categoria = categoria, 
                                    sabor = sabor,
                                    data_validade = data_validade)
            session.add(suplemento)
            session.commit()
            print(f"{nome} adcionado ao estoque")

    def listar_produtos(self):
        with Session(engine) as session:
            produtos = session.query(Produto).all()
            if produtos:
                for produto in produtos:
                    print(produto)
            else:
                print("Não ha produtos cadastrados!")

    def buscar_produto(self, nome):
        with Session(engine) as session:
            produto = session.query(Produto).filter(Produto.nome.ilike(nome)).first()
            return produto

    def realizar_venda(self, nome, quantidade):
        with Session(engine) as session:
            produto = session.query(Produto).filter(Produto.nome.ilike(nome)).first()
            if produto is None:
                print("Produto não encontrado!")
                return
            if produto.quantidade < quantidade:
                print("Quantidade insuficiente!")
                return

            produto.quantidade -= quantidade
            venda = Venda(produto_id = produto.id, 
                          quantidade = quantidade, 
                          preco_total = produto.preco * quantidade)
            session.add(venda)
            session.commit()
            print(f"Venda realizada! Total: R${venda.preco_total}")


    def repor_estoque(self, nome, quantidade):
        with Session(engine) as session:
            produto = session.query(Produto).filter(Produto.nome.ilike(nome)).first()
            if produto is None:
                print("Produto não encontrado!")
                return
            
            produto.quantidade += quantidade
            session.commit()
            print("Produto adcionado com sucesso")

    def deletar_produto(self, nome):
        with Session(engine) as session:
            produto = session.query(Produto).filter(Produto.nome.ilike(nome)).first()
            if produto is None:
                print("❌ Produto não encontrado!")
                return
            session.delete(produto)
            session.commit()
            print(f"{produto.nome} removido do estoque!")

    def listar_vendas(self):
        with Session(engine) as session:
            vendas = session.query(Venda).all()
            if vendas:
                for venda in vendas:
                    print(venda)
            else:
                print("0 vendas registradas!") 

    def relatorio_vendas(self):
        with Session(engine) as session:
            vendas = session.query(Venda).all()
            if not vendas:
                print("Nenhuma venda realizada!")
                return
            total = sum(float(venda.preco_total)for venda in vendas)
            print(f"Total de vendas:{len(vendas)}")
            print(f"Valor total: R${total:.2f}")