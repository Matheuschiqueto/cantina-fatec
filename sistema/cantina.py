from sistema.estoque import Estoque
from sistema.historico_pagamento import HistoricoPagamento
from modelos.pagamento import Pagamento
from sistema.relatorios import Relatorios
import pickle
import os

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
            novo_pix = Pagamento(nome_cliente, categoria, curso, valor_total, nome_produto, quantidade)
            self.historico.registrar_pagamento(novo_pix)
            print("Venda concluída com sucesso!")
        else:
            print("Venda cancelada: Quantidade insuficiente no lote atual.")

    def salvar_dados(self):
        """Salva o estado atual do estoque e histórico em um arquivo binário."""
        try:
            with open("dados_cantina.dat", "wb") as arquivo:
                dados = {
                    "estoque": self.estoque,
                    "historico": self.historico
                }
                pickle.dump(dados, arquivo)
            print("\n Dados salvos com sucesso!")
        except Exception as e:
            print(f"\n Erro ao salvar dados: {e}")

    def carregar_dados(self):
        """Tenta carregar os dados salvos anteriormente."""
        if os.path.exists("dados_cantina.dat"):
            try:
                with open("dados_cantina.dat", "rb") as arquivo:
                    dados = pickle.load(arquivo)
                    self.estoque = dados["estoque"]
                    self.historico = dados["historico"]
                print("\n Dados carregados do arquivo 'dados_cantina.dat'.")
                return True
            except Exception as e:
                print(f"\n Erro ao carregar arquivo: {e}")
        return False
    
    def adicionar_ao_estoque(self, produto):
        self.estoque.cadastrar_produto(produto)