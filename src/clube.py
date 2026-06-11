class Clube:

    def __init__(self, nome, tecnico):
        self.nome = nome
        self.tecnico = tecnico
        self.jogadores = []

        self.pontos = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0

        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def saldo_gols(self):
        return self.gols_marcados - self.gols_sofridos

    def mostrar_elenco(self):
        print(f"\nElenco do {self.nome}")

        for jogador in self.jogadores:
            print(jogador.apresentar())