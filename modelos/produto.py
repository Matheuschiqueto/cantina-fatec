class Produto:
    
    def __init__(self, nome, preco_custo, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.__quantidade = quantidade

    def get_quantidade(self):
        """Retorna a quantidade atual em estoque."""
        return self.__quantidade

    def set_quantidade(self, nova_quantidade):
        """
        Edita a quantidade em estoque.
        """
        if nova_quantidade < 0:
            print(f"Erro: A quantidade de '{self.nome}' não pode ser negativa!")
        else:
            self.__quantidade = nova_quantidade

    def __str__(self):
        """Imprime o objeto."""
        return f"{self.nome} | Qtd: {self.__quantidade} | Vence em: {self.data_vencimento} | Preço: R$ {self.preco_venda:.2f}"