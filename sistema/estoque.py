from estruturas.fila import Fila

class Estoque:
    """Classe responsável por gerenciar a inteligência do estoque da Cantina."""
    
    def __init__(self):
        self.prateleiras = {}

    def cadastrar_produto(self, produto):
        """Adiciona um novo produto ao estoque, na sua fila específica."""
        # Se a prateleira para esse produto não existe, cria uma nova Fila
        if produto.nome not in self.prateleiras:
            self.prateleiras[produto.nome] = Fila()
            
        self.prateleiras[produto.nome].enfileirar(produto)
        print(f"Produto cadastrado: {produto.nome} (Lote com {produto.get_quantidade()} unidades)")

    def vender_produto(self, nome_produto, quantidade_comprada):
        """
        Vende uma quantidade de um produto específico.
        Consome do lote mais antigo primeiro (FIFO).
        """
        # Verifica se o produto existe e se a fila não está vazia
        if nome_produto not in self.prateleiras or self.prateleiras[nome_produto].esta_vazia():
            print(f"Erro: Não temos {nome_produto} no estoque!")
            return False
            
        fila_do_produto = self.prateleiras[nome_produto]
        
        # Pega o primeiro da fila (mais velho) APENAS PARA OLHAR, sem tirar da fila ainda!
        lote_mais_velho = fila_do_produto.ver_primeiro() 
        qtd_disponivel = lote_mais_velho.get_quantidade()
        
        if quantidade_comprada <= qtd_disponivel:
            nova_qtd = qtd_disponivel - quantidade_comprada
            lote_mais_velho.set_quantidade(nova_qtd)
            print(f"Venda confirmada: {quantidade_comprada}x {nome_produto}.")
            
            # Se o lote zerar depois da venda, remove ele da fila
            if lote_mais_velho.get_quantidade() == 0:
                fila_do_produto.desenfileirar()
                print(f"Aviso: O lote de {nome_produto} que vencia em {lote_mais_velho.data_vencimento} acabou e foi removido do estoque.")
            
            return True
        else:
            print(f"Erro: O lote mais velho de {nome_produto} só tem {qtd_disponivel} unidades. Peça uma quantidade menor.")
            return False

    def listar_estoque(self):
        """Exibe todos os produtos cadastrados atualmente, separados por tipo."""
        if not self.prateleiras:
            print("Estoque vazio.")
            return

        print("\n--- PRODUTOS NO ESTOQUE ---")
        for nome, fila in self.prateleiras.items():
            if not fila.esta_vazia():
                print(f"\n[{nome.upper()}]")
                for produto in fila.listar_todos():
                    print(f"  -> {produto}")
        print("------------------------------\n")