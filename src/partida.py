class Partida:

    def __init__(self, time_casa, time_visitante):
        self.time_casa = time_casa
        self.time_visitante = time_visitante

        self.gols_casa = 0
        self.gols_visitante = 0

    def registrar_resultado(self, gols_casa, gols_visitante):
        self.gols_casa = gols_casa
        self.gols_visitante = gols_visitante

        #atualiza gols do time da casa
        self.time_casa.gols_marcados += gols_casa
        self.time_casa.gols_sofridos += gols_visitante

        #atualiza gols do visitante
        self.time_visitante.gols_marcados += gols_visitante
        self.time_visitante.gols_sofridos += gols_casa

        #vitória do time da casa
        if gols_casa > gols_visitante:
            self.time_casa.pontos += 3
            self.time_casa.vitorias += 1

            self.time_visitante.derrotas += 1

        #vitória do visitante
        elif gols_visitante > gols_casa:
            self.time_visitante.pontos += 3
            self.time_visitante.vitorias += 1

            self.time_casa.derrotas += 1

        #empate
        else:
            self.time_casa.pontos += 1
            self.time_visitante.pontos += 1

            self.time_casa.empates += 1
            self.time_visitante.empates += 1