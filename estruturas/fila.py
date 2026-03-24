class Fila:
    def __init__(self):
        self._itens = []

    def esta_vazia(self):
        """Verifica se a fila não tem ninguém"""
        return len(self._itens) == 0

    def enfileirar(self, item):
        """Coloca um novo item no final da fila"""
        self._itens.append(item)

    def desenfileirar(self):
        """Tira e retorna o item que está no início da fila (o mais velho)"""
        if self.esta_vazia():
            return None
        return self._itens.pop(0) 
    
    def ver_primeiro(self):
        """Só olha quem é o primeiro da fila, sem tirar ele de lá"""
        if self.esta_vazia():
            return None
        return self._itens[0]

    def listar_todos(self):
        """
        Retorna uma cópia da fila para gerar os relatórios.
        """
        return list(self._itens)