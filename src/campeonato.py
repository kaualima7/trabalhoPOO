from partida import Partida

class Campeonato:

    def __init__(self, nome):
        self._nome = nome
        self._times = []
        self._partidas = []

    @property
    def nome(self):
        return self._nome

    @property
    def times(self):
        return list(self._times)

    @property
    def partidas(self):
        return list(self._partidas)

    def adicionar_time(self, time):
        self._times.append(time)

    def adicionar_partida(self, time_casa, time_visitante, gols_casa, gols_visitante):
        partida = Partida(time_casa, time_visitante)
        partida.registrar_resultado(gols_casa, gols_visitante)
        self._partidas.append(partida)

    def mostrar_tabela(self):
        tabela = sorted(
            self._times,
            key=lambda t: (
                t.pontos,
                t.saldo_gols(),
                t.gols_marcados
            ),
            reverse=True
        )

        print(f"\n=== TABELA DO {self._nome.upper()} ===")
        for posicao, time in enumerate(tabela, start=1):
            print(
                f"{posicao}º - {time.nome} | "
                f"{time.pontos} pts | "
                f"SG: {time.saldo_gols()}"
            )

    def definir_campeao(self):
        campeao = sorted(
            self._times,
            key=lambda t: (
                t.pontos,
                t.saldo_gols(),
                t.gols_marcados
            ),
            reverse=True
        )[0]

        return campeao