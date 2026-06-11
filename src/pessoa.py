class Pessoa:

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Nome não pode ser vazio.")
        self._nome = valor.strip()

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("Idade deve ser um número inteiro positivo.")
        self._idade = valor

    def apresentar(self):
        return f"Nome: {self._nome} | Idade: {self._idade}"