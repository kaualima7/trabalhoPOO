from jogador import Jogador
from tecnico import Tecnico
from clube import Clube
from partida import Partida
from campeonato import Campeonato


#Função pra criar lista dos jogadores
def criar_jogadores(lista_nomes):
    jogadores = []

    for numero, nome in enumerate(lista_nomes, start=1):
        jogadores.append(
            Jogador(
                nome,
                25,
                numero,
                "Jogador"
            )
        )
    return jogadores

nomes_gremio = [
    "Weverton",
    "Pavon",
    "Viery",
    "Gustavo Martins",
    "Marlon",
    "Noriega",
    "Leo Perez",
    "Gabriel Mec",
    "Enamorado",
    "Carlos Vinicius",
    "Amuzu"
]

nomes_brasil = [
    "Alisson",
    "Danilo",
    "Marquinhos",
    "Gabriel Magalhaes",
    "Alex Sandro",
    "Casemiro",
    "Bruno Guimaraes",
    "Neymar",
    "Raphinha",
    "Vinicius Junior",
    "Rayan"
]

print("===================================")
print(" SISTEMA DA COPA AMISTOSA ")
print("===================================")

##############################################################
# Técnicos
print("\nCriando técnicos...")

tecnico_gremio = Tecnico(
    "Luís Castro",
    64,
    "Nem ele sabe",
    30
)

tecnico_brasil = Tecnico(
    "Carlo Ancelotti",
    67,
    "Equilibrada",
    40
)

print(tecnico_gremio.apresentar())
print(tecnico_brasil.apresentar())

##############################################################
# Clube/Seleção
print("Criando clubes...")

gremio = Clube(
    "Gremio",
    tecnico_gremio
)

brasil = Clube(
    "Brasil",
    tecnico_brasil
)

print("Criando jogadores...")

jogadores_gremio = criar_jogadores(nomes_gremio)
jogadores_brasil = criar_jogadores(nomes_brasil)

print("Adicionando jogadores aos clubes...")

for jogador in jogadores_gremio:
    gremio.adicionar_jogador(jogador)

for jogador in jogadores_brasil:
    brasil.adicionar_jogador(jogador)

print("\n=== ELENCOS ===")
gremio.mostrar_elenco()
brasil.mostrar_elenco()

# Campeonato
print("\nCriando campeonato...")

campeonato = Campeonato("Copa Amistosa")

campeonato.adicionar_time(gremio)
campeonato.adicionar_time(brasil)

print("\n=== ANTES DA PARTIDA ===")
print(f"{gremio.nome}: {gremio.pontos} pontos")
print(f"{brasil.nome}: {brasil.pontos} pontos")

jogadores_gremio[9].fazer_gol()
print(
    f"\n{jogadores_gremio[9].nome} marcou um gol!"
)

jogadores_brasil[5].fazer_gol()
print(
    f"\n{jogadores_brasil[5].nome} marcou um gol"
)

jogadores_gremio[10].fazer_gol()
print(
    f"\n{jogadores_gremio[10].nome} marcou um gol"
)

# Partida
print("\nRegistrando partida...")

partida1 = Partida(gremio, brasil)

partida1.registrar_resultado(2, 1)

print("\n=== DEPOIS DA PARTIDA ===")
print(f"{gremio.nome}: {gremio.pontos} pontos")
print(f"{brasil.nome}: {brasil.pontos} pontos")

campeonato.adicionar_partida(partida1)

print("\nResultado:")
print(f"{gremio.nome} 2 x 1 {brasil.nome}")

# Tabela
campeonato.mostrar_tabela()

# Campeão
campeao = campeonato.definir_campeao()

print("\n=== CAMPEÃO ===")
print(campeao.nome)
print(f"Pontos: {campeao.pontos}")
print(f"Saldo de gols: {campeao.saldo_gols()}")