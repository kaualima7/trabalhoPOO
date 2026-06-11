from jogador import Jogador
from tecnico import Tecnico
from clube import Clube
from partida import Partida

t1 = Tecnico("Abel", 46, "Ofensiva", 15)
t2 = Tecnico("Renato", 62, "Defensiva", 20)

j1 = Jogador("Neymar", 33, 10, "Atacante")
j2 = Jogador("Casemiro", 32, 5, "Volante")
j3 = Jogador("Endrick", 19, 18, "Atacante")

clube1 = Clube("Brasil", t1)
clube2 = Clube("Gremio FBPA", t2)

clube1.adicionar_jogador(j1)
clube1.adicionar_jogador(j2)

clube2.adicionar_jogador(j3)

partida1 = Partida(clube1, clube2)

partida1.registrar_resultado(2, 1)

print(f"{clube1.nome}: {clube1.pontos} pontos")
print(f"{clube2.nome}: {clube2.pontos} pontos")