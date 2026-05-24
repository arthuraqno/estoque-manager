from models.equipamento import Equipamento
from models.produto import Produto
from models.suplemento import Suplemento
from models.venda import Venda
from services.estoque import Estoque

estoque = Estoque()
estoque.carregar_dados()

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
                produto = Equipamento(nome, preco, quantidade, categoria, tamanho)
                estoque.cadastrar_equipamento(produto)
            else:
                sabor = input("Sabor: ")
                data_validade = input("Data de validade (AAAA-MM-DD): ")
                produto = Suplemento(nome, preco, quantidade, categoria, sabor, data_validade)
                estoque.cadastrar_suplemento(produto)

        elif opcao == "2":
            nome = input("Nome do produto: ")
            produto = estoque.buscar_produto(nome)
            if produto is None:
                print(" Produto não encontrado.")
            else:
                quantidade = int(input("Quantidade: "))
                estoque.realizar_venda(produto, quantidade)

        elif opcao == "3":
            nome = input("Nome do produto: ")
            produto = estoque.buscar_produto(nome)
            if produto is None:
                print(" Produto não encontrado.")
            else:
                quantidade = int(input("Quantidade a repor: "))
                estoque.repor_estoque(produto, quantidade)

        elif opcao == "4":
            nome = input("Nome do produto: ")
            produto = estoque.buscar_produto(nome)
            if produto is None:
                print(" Produto não encontrado.")
            else:
                estoque.deletar_produto(produto)

        elif opcao == "5":
            estoque.listar_produtos()

        elif opcao == "6":
            estoque.listar_vendas()

        elif opcao == "7":
            estoque.salvar_dados()
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print(" Opção inválida.")

menu()