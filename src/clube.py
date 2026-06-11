class Clube:

    def __init__(self, nome, tecnico):
        self._nome = nome
        self._tecnico = tecnico
        self._jogadores = []

        self._pontos = 0
        self._gols_marcados = 0
        self._gols_sofridos = 0

        self._vitorias = 0
        self._empates = 0
        self._derrotas = 0

    @property
    def nome(self):
        return self._nome

    @property
    def tecnico(self):
        return self._tecnico

    @property
    def jogadores(self):
        return list(self._jogadores)

    @property
    def pontos(self):
        return self._pontos

    @property
    def gols_marcados(self):
        return self._gols_marcados

    @property
    def gols_sofridos(self):
        return self._gols_sofridos

    @property
    def vitorias(self):
        return self._vitorias

    @property
    def empates(self):
        return self._empates

    @property
    def derrotas(self):
        return self._derrotas

    def adicionar_jogador(self, jogador):
        self._jogadores.append(jogador)

    def saldo_gols(self):
        return self._gols_marcados - self._gols_sofridos

    def registrar_vitoria(self, gols_marcados, gols_sofridos):
        self._gols_marcados += gols_marcados
        self._gols_sofridos += gols_sofridos
        self._pontos += 3
        self._vitorias += 1

    def registrar_empate(self, gols_marcados, gols_sofridos):
        self._gols_marcados += gols_marcados
        self._gols_sofridos += gols_sofridos
        self._pontos += 1
        self._empates += 1

    def registrar_derrota(self, gols_marcados, gols_sofridos):
        self._gols_marcados += gols_marcados
        self._gols_sofridos += gols_sofridos
        self._derrotas += 1

    def mostrar_elenco(self):
        print(f"\nElenco do {self._nome}")
        for jogador in self._jogadores:
            print(jogador.apresentar())