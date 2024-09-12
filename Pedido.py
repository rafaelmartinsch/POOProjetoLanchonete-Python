class Pedido:

    def __init__(self, numero,data,hora,pagamento,cliente) -> None:
        self.numero=numero
        self.data=data
        self.hora=hora
        self.pagamento=pagamento
        self.cliente=cliente
        self.status="Aberto"


    def imprimir(self):
        print(f"----- Pedido n° {self.numero} -----\n"
              f"Data:{self.data} - Horário: {self.hora} \n"
              f"Status: {self.status}\n"
              f"Forma de Pagamento: {self.pagamento} \n"
              f"Cliente: {self.cliente.nome}"
              f"| Endereço: {self.cliente.endereco}"
              f"| Telefone: {self.cliente.telefone}"
            )