class Lista:
    def __init__(self):
        self._itens = []

    def esta_vazia(self):
        """Verifica se a lista está vazia."""
        return len(self._itens) == 0

    def adicionar(self, item):
        """Adiciona um novo item ao final da lista."""
        self._itens.append(item)

    def tamanho(self):
        """Retorna a quantidade de itens salvos na lista."""
        return len(self._itens)

    def listar_todos(self):
        """
        Retorna uma cópia dos itens.
        """
        return list(self._itens)