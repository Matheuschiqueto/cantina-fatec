from sistema.estoque import Estoque
from sistema.historico_pagamento import HistoricoPagamento
from modelos.pagamento import Pagamento

class Cantina:
    """Classe principal que une o Estoque e os Pagamentos."""

    def __init__(self):
        self.estoque = Estoque()
        self.historico = HistoricoPagamento()

    def realizar_venda(self, nome_cliente, categoria, curso, nome_produto, quantidade):
        """Simula a jornada completa de um aluno comprando algo."""
        print(f"\nIniciando venda de {quantidade}x {nome_produto} para {nome_cliente}...")

        if nome_produto not in self.estoque.prateleiras or self.estoque.prateleiras[nome_produto].esta_vazia():
            print(f"Venda cancelada: Não temos {nome_produto}.")
            return

        produto_lote = self.estoque.prateleiras[nome_produto].ver_primeiro()
        valor_total = produto_lote.preco_venda * quantidade

        sucesso_estoque = self.estoque.vender_produto(nome_produto, quantidade)

        if sucesso_estoque:
            novo_pix = Pagamento(nome_cliente, categoria, curso, valor_total)
            self.historico.registrar_pagamento(novo_pix)
            print("Venda concluída com sucesso!")
        else:
            print("Venda cancelada: Quantidade insuficiente no lote atual.")