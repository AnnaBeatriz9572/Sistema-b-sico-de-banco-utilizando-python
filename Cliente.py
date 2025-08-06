class Cliente:
    def __init__(self, n, fone):
        self._nome = n #podem ser acessados
        self._telefone = fone #podem ser acessados

    #metodo get
    @property
    def get_nome(self):
        return self._nome

    @get_nome.setter
    #metodo set
    def set_nome(self, nome):
        self._nome = nome
