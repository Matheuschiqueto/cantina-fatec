from estruturas.fila import Fila

class Estoque:
    """Classe responsável por gerenciar a inteligência do estoque da Cantina."""
    
    def __init__(self):
        self.produtos = Fila()

    def cadastrar_produto(self, produto):
        """Adiciona um novo produto ao estoque."""
        self.produtos.enfileirar(produto)
        print(f"Produto cadastrado: {produto.nome}")

    def retirar_para_venda(self):
        """
        Remove e retorna o produto mais antigo para a venda.
        Garante a regra de prioridade para os produtos mais velhos.
        """
        if self.produtos.esta_vazia():
            print("Erro: O estoque está vazio!")
            return None
        
        produto_mais_velho = self.produtos.desenfileirar()
        return produto_mais_velho

    def listar_estoque(self):
        """Exibe todos os produtos cadastrados atualmente."""
        if self.produtos.esta_vazia():
            print("Estoque vazio.")
            return

        print("\n--- PRODUTOS NO ESTOQUE ---")
        
        for produto in self.produtos.listar_todos():
            print(produto)
        print("------------------------------\n")