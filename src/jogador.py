from pessoa import Pessoa


class Jogador(Pessoa):

    def __init__(self, nome, idade, numero_camisa, posicao):
        super().__init__(nome, idade)
        self.numero_camisa = numero_camisa
        self.posicao = posicao
        self.gols = 0

    def fazer_gol(self):
        self.gols += 1

    def apresentar(self):
        return (
            f"Jogador: {self.nome} | "
            f"Camisa: {self.numero_camisa} | "
            f"Posição: {self.posicao} | "
            f"Gols: {self.gols}"
        )