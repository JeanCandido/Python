tabela = {
        "Alface": [6.00, 30],
        "Tomate": [11.00, 40],
        "Batata": [9.00, 20],
    }

carrinho = 0

lista_compras = ""

while True:

    produto = input("Selcione um produto: ").capitalize()
    
    if produto not in tabela:
        print("Produto não encontrado.")
        continue
    
    estoque = tabela[produto][1]
    
    
    if estoque <= 0:
        print("Produto em falta.")
        continue
    
    quantidade = float(input("Qual é a quantidade: "))
    
    if quantidade >= estoque:
        print(f"A quantidade total do nosso estoque é {estoque} escolha uma quantidade igual ou menor.\n")
        continue

    valor_produto = tabela[produto][0]
    

    valor_produto_total = valor_produto * quantidade

    tabela[produto] = (valor_produto, estoque - quantidade)

    carrinho += valor_produto_total
    
    lista_compras += f"{produto}: R${valor_produto_total}\n"
    
    print(f"R${valor_produto_total}")
    
    adicionar_carrinho = input("Quer adicionar mais items?(s/n): ")
    
    if adicionar_carrinho == "s":
        continue
    else:
        print("\nListas de compras:")
        print(lista_compras)
        print(f"Total: R${carrinho}\n")
        print("Volte sempre.")
        break