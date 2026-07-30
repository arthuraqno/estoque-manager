from models.equipamento import Equipamento
from models.produto import Produto
from models.suplemento import Suplemento
from models.venda import Venda
from services.estoque import Estoque

estoque = Estoque()

def menu():
    while True:
        print("\n=====================================")
        print("       💻  ESTOQUE MANAGER")
        print("=====================================")
        print("1. Cadastrar produto")
        print("2. Vender produto")
        print("3. Repor estoque")
        print("4. Deletar produto")
        print("5. Listar produtos")
        print("6. Listar vendas")
        print("7. Sair")
        print("=====================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: R$"))
            quantidade = int(input("Quantidade: "))
            categoria = input("Categoria (equipamento/suplemento): ").lower()
            if categoria == "equipamento":
                tamanho = input("Tamanho (A0/A1/A2/A3/A4): ")
                estoque.cadastrar_equipamento(nome, preco, quantidade, categoria, tamanho)
            else:
                sabor = input("Sabor: ")
                data_validade = input("Data de validade (AAAA-MM-DD): ")
                estoque.cadastrar_suplemento(nome, preco, quantidade, categoria, sabor, data_validade)

        elif opcao == "2":
            nome = input("Nome do produto: ")
            produto = estoque.buscar_produto(nome)
            if produto is None:
                print(" Produto não encontrado.")
            else:
                quantidade = int(input("Quantidade: "))
                estoque.realizar_venda(nome, quantidade)

        elif opcao == "3":
            nome = input("Nome do produto: ")
            produto = estoque.buscar_produto(nome)
            if produto is None:
                print(" Produto não encontrado.")
            else:
                quantidade = int(input("Quantidade a repor: "))
                estoque.repor_estoque(nome, quantidade)

        elif opcao == "4":
            nome = input("Nome do produto: ")
            produto = estoque.buscar_produto(nome)
            if produto is None:
                print(" Produto não encontrado.")
            else:
                estoque.deletar_produto(nome)

        elif opcao == "5":
            estoque.listar_produtos()

        elif opcao == "6":
            estoque.listar_vendas()

        elif opcao == "7":
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print(" Opção inválida.")

menu()