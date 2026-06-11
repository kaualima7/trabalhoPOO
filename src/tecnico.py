from pessoa import Pessoa

class Tecnico(Pessoa):

    def __init__(self, nome, idade, estrategia, anos_experiencia):
        super().__init__(nome, idade)
        self._estrategia = estrategia
        self._anos_experiencia = anos_experiencia

    @property
    def estrategia(self):
        return self._estrategia

    @estrategia.setter
    def estrategia(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Estratégia não pode ser vazia.")
        self._estrategia = valor.strip()

    @property
    def anos_experiencia(self):
        return self._anos_experiencia

    @anos_experiencia.setter
    def anos_experiencia(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("Anos de experiência não pode ser negativo.")
        self._anos_experiencia = valor

    def apresentar(self):
        return (
            f"Técnico: {self._nome} | "
            f"Estratégia: {self._estrategia} | "
            f"Experiência: {self._anos_experiencia} anos"
        )