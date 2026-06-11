from jogador import Jogador
from tecnico import Tecnico
from clube import Time

j1 = Jogador("Neymar", 33, 10, "Atacante")
j2 = Jogador("Casemiro", 32, 5, "Volante")

t1 = Tecnico("Abel", 46, "Ofensiva", 15)

time1 = Time("Brasil FC", t1)

time1.adicionar_jogador(j1)
time1.adicionar_jogador(j2)

time1.mostrar_elenco()

print("\nSaldo de gols:")
print(time1.saldo_gols())