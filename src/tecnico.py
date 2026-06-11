from pessoa import Pessoa

class Tecnico(Pessoa):

    def __init__(self, nome, idade, estrategia, anos_experiencia):
        super().__init__(nome, idade)
        self.estrategia = estrategia
        self.anos_experiencia = anos_experiencia

    def apresentar(self):
        return (
            f"Técnico: {self.nome} | "
            f"Estratégia: {self.estrategia} | "
            f"Experiência: {self.anos_experiencia} anos"
        )