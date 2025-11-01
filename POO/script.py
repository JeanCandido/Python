class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos

    def increver(self, quantidade=1):
        self.inscritos += quantidade    

canal_lancode = Canal('Lan Code', 'Codigos e Gatos', 34000)
canal_guanabara = Canal('Curso em Video', 'Paixẽo por ensinar', 2500000)

print(f"Quantidade de inscritos atuais: {canal_lancode.inscritos}")
canal_lancode.increver(500)
print(f"Quantidade de inscritos atuais: {canal_lancode.inscritos}")
