class Partida:

    def __init__(self, time_casa, time_visitante):
        self._time_casa = time_casa
        self._time_visitante = time_visitante

        self._gols_casa = 0
        self._gols_visitante = 0

    @property
    def time_casa(self):
        return self._time_casa

    @property
    def time_visitante(self):
        return self._time_visitante

    @property
    def gols_casa(self):
        return self._gols_casa

    @property
    def gols_visitante(self):
        return self._gols_visitante

    def registrar_resultado(self, gols_casa, gols_visitante):
        if gols_casa < 0 or gols_visitante < 0:
            raise ValueError("Número de gols não pode ser negativo.")

        self._gols_casa = gols_casa
        self._gols_visitante = gols_visitante

        #vitória do time da casa
        if gols_casa > gols_visitante:
            self._time_casa.registrar_vitoria(gols_casa, gols_visitante)
            self._time_visitante.registrar_derrota(gols_visitante, gols_casa)

        #vitória do visitante
        elif gols_visitante > gols_casa:
            self._time_visitante.registrar_vitoria(gols_visitante, gols_casa)
            self._time_casa.registrar_derrota(gols_casa, gols_visitante)

        #empate
        else:
            self._time_casa.registrar_empate(gols_casa, gols_visitante)
            self._time_visitante.registrar_empate(gols_visitante, gols_casa)