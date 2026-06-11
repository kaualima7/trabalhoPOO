from pessoa import Pessoa

class Jogador(Pessoa):
    def __init__(self, nome, idade, numero_camisa, posicao):
        super().__init__(nome, idade)
        self._numero_camisa = numero_camisa
        self._posicao = posicao
        self._gols = 0

    @property
    def numero_camisa(self):
        return self._numero_camisa

    @numero_camisa.setter
    def numero_camisa(self, valor):
        if not isinstance(valor, int) or not (1 <= valor <= 99):
            raise ValueError("Número da camisa deve estar entre 1 e 99.")
        self._numero_camisa = valor

    @property
    def posicao(self):
        return self._posicao

    @posicao.setter
    def posicao(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Posição não pode ser vazia.")
        self._posicao = valor.strip()

    @property
    def gols(self):
        return self._gols

    def fazer_gol(self):
        self._gols += 1

    def apresentar(self):
        return (
            f"Jogador: {self._nome} | "
            f"Camisa: {self._numero_camisa} | "
            f"Posição: {self._posicao} | "
            f"Gols: {self._gols}"
        )