class Campeonato:

    def __init__(self, nome):
        self.nome = nome
        self.times = []
        self.partidas = []

    def adicionar_time(self, time):
        self.times.append(time)

    def adicionar_partida(self, partida):
        self.partidas.append(partida)

    def mostrar_tabela(self):
        tabela = sorted(
            self.times,
            key=lambda t: (
                t.pontos,
                t.saldo_gols(),
                t.gols_marcados
            ),
            reverse=True
        )

        print(f"\n=== TABELA DO {self.nome.upper()} ===")
        for posicao, time in enumerate(tabela, start=1):

            print(
                f"{posicao}º - {time.nome} | "
                f"{time.pontos} pts | "
                f"SG: {time.saldo_gols()}"
            )

    def definir_campeao(self):
        campeao = sorted(
            self.times,
            key=lambda t: (
                t.pontos,
                t.saldo_gols(),
                t.gols_marcados
            ),
            reverse=True
        )[0]

        return campeao