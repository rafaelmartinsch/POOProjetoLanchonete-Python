from Produto import Produto
from Cliente import Cliente
from Pedido import Pedido
from datetime import datetime

listaProdutos = [] 
listaClientes = []

def buscarProduto(buscaCod):
    i = 0
    for objetoBusca in listaProdutos:
        if objetoBusca.cod==buscaCod:
            return objetoBusca, i
        i+=1
    return None, i

def buscarCliente(buscaCPF):
    i = 0
    for objetoBusca in listaClientes:
        if objetoBusca.cpf==buscaCPF:
            return objetoBusca, i
        i+=1
    return None, i

def menuProdutos():
    while(True):
        print("\n\nBEM VINDO AO SISTEMA DE PRODUTOS")
        print("Escolha uma opção: \n"
            "1 - 💾 Cadastrar Produto\n"
            "2 - 🔎 Listar Produtos\n"
            "3 - ✏️ Alterar Produto\n"
            "4 - ❌ Excluir Produto\n"
            "0 - ⬅️ Voltar ")
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
        
            produto, posicao = buscarProduto(codigo)
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
        
            produto, posicao = buscarProduto(codigo)
            if produto is None:
                print("Produto Não encontrado!")
            else:
                listaProdutos.pop(posicao)
                print("Produto Excluído com Sucesso!")


        else:
            print("Opção Inválida!")
    ##fim while

def menuClientes():
    while(True):
        print("\n\n 👤BEM VINDO AO SISTEMA DE CLIENTES")
        print("Escolha uma opção: \n"
            "1 - 💾 Cadastrar Cliente\n"
            "2 - 🔎 Listar Cliente\n"
            "3 - ✏️ Alterar Cliente\n"
            "0 - ⬅️ Voltar ")
        escolha = input("Digite:")

        if escolha=="0":
            break

        elif escolha=="1":
            print("\n\n💾 CADASTRO DE CLIENTE:")
        
            cpf=input("CPF:")
            nome=input("Nome Cliente:")
            telefone=input("Telefone:")
            endereco=input("Endereço:")

            objetoCliente = Cliente(cpf=cpf, endereco=endereco, telefone=telefone, nome=nome) ##quando especifico o atributo não precisa seguir a ordem dos parametros
            listaClientes.append(objetoCliente)

        elif escolha=="2":
            print("\n\n🔎 LISTA DE CLIENTES CADASTRADOS:")
            for objetoCliente in listaClientes:
                objetoCliente.imprimir()

        elif escolha=="3":
            print("\n\n✏️ ALTERAR INFORMAÇÕES SOBRE UM CLIENTE:")
            cpf =  input("Informe o CPF do cliente:")
        
            cliente, posicao = buscarCliente(cpf)
            if cliente is None:
                print("Cliente Não encontrado!")
            else:
                nome=input("Nome Cliente:")
                telefone=input("Telefone:")
                endereco=input("Endereço:")
                cliente.alterar(nome, telefone, endereco)

                listaClientes[posicao]=cliente

                print("Produto excluído com sucesso!")

        else:
            print("Opção Inválida!")
    ##fim while


while(True):
    print("\n\n BEM VINDO AO SISTEMA DE LANCHONETE")
    print("Escolha uma opção: \n"
        "1 - 👤 Clientes \n"
        "2 - 📦 Produtos \n"
        "3 - 🛒 Novo Pedido \n"
        "0 - ⬅️ Sair ")
    escolha = input("Digite:")

    if escolha=="0":
        break
    elif escolha=="1":
        menuClientes()
    elif escolha=="2":
        menuProdutos()

    elif escolha=="3":

        

        data = datetime.now().strftime('%d/%m/%Y')
        hora = datetime.now().strftime('%H:%M')
        pagamento="PiXX"

        objetoCliente=listaClientes[0]

        objetoPedido = Pedido(1, data, hora, pagamento,objetoCliente)
        objetoPedido.imprimir()
    else:
         print("Opção Inválida!")


print("\n bye! \n ( >‿◠ )✌")