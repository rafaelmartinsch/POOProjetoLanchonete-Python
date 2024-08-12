from Produto import Produto
    

def buscar(buscaCod):
    i = 0
    for objetoBusca in listaProdutos:
        if objetoBusca.cod==buscaCod:
            return objetoBusca, i
        i+=1
    return None, i

listaProdutos = []

while(True):
    print("\n\nBEM VINDO AO SISTEMA DE PRODUTOS")
    print("Escolha uma opção: \n"
        "1 - 💾 Cadastrar \n"
        "2 - 🔎 Listar \n"
        "3 - ✏️ Alterar \n"
        "4 - ❌ Excluir \n"
        "0 - ⬅️ Sair ")
    escolha = input("Digite:")

    if escolha=="0":
         break
    

    elif escolha=="1":
        print("\n\n💾 CADASTRO DE PRODUTOS:")
    
        codigo=input("Código do Produto:")
        descricao=input("Descrição do Produto:")
        preco=float(input("Preço R$:"))
        qtd=int(input("Quantidade em Estoque:"))

        objetoProduto = Produto(codigo,descricao, preco, qtd)
        listaProdutos.append(objetoProduto)


    elif escolha=="2":
        print("\n\n🔎 LISTA DE PRODUTOS CADASTRADOS:")
        for produto in listaProdutos:
            produto.listar()


    elif escolha=="3":
        print("\n\n✏️ ALTERAR INFORMAÇÕES SOBRE UM PRODUTO:")
        codigo =  input("Informe o Codigo do Produto:")
    
        produto, posicao = buscar(codigo)
        if produto is None:
            print("Produto Não encontrado!")
        else:
            descricao=input("Descrição do Produto:")
            preco=float(input("Preço R$:"))
            qtd=int(input("Quantidade em Estoque:"))
            produto.alterar(descricao, preco, qtd)

            listaProdutos[posicao]=produto

            print("Produto excluído com sucesso!")


    elif escolha=="4":
        print("\n\n❌ EXCLUIR PRODUTO:")
        codigo =  input("Informe o Codigo do Produto:")
    
        produto, posicao = buscar(codigo)
        if produto is None:
            print("Produto Não encontrado!")
        else:
            listaProdutos.pop(posicao)
            print("Produto Excluído com Sucesso!")


    else:
        print("Opção Inválida!")

print("\n bye! \n ( >‿◠ )✌")