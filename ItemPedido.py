class ItemPedido:


    def __init__(self, produto, quantidade, observacao, desconto ):
        self.produto=produto
        self.qtd=quantidade
        self.obs=observacao
        self.desconto=desconto

    def imprime(self):
        print(
              f"Produto: {self.produto.descricao}"
              f"| Qtd: {self.qtd}"
              f"| Desconto: {self.desconto}"
              f"| Observação: {self.obs}"
            )