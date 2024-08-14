class Cliente:

    def __init__(self, cpf, nome, telefone, endereco) -> None:
        self.nome=nome
        self.cpf=cpf
        self.telefone=telefone
        self.endereco=endereco
    
    def alterar(self, nome, telefone, endereco):
        self.nome=nome
        self.telefone=telefone
        self.endereco=endereco

    def imprimir(self):
         print(  f" cpf: {self.cpf}"+
                f" | Nome: {self.nome[:20]:<20}"
                f" | Telefone: {self.telefone}"+
                f" | endereço: {self.endereco}")