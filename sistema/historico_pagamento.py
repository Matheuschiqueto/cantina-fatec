from estruturas.lista import Lista

class HistoricoPagamento:
    """Gerencia todos os pagamentos realizados na cantina."""

    def __init__(self):
        self.pagamentos = Lista()

    def registrar_pagamento(self, pagamento):
        """Salva um novo pagamento no final do histórico."""
        self.pagamentos.adicionar(pagamento)
        print(f"Pagamento recebido: R$ {pagamento.valor:.2f} de {pagamento.nome}")

    def listar_pagamentos(self):
        """Exibe o extrato completo de todos os pagamentos."""
        if self.pagamentos.esta_vazia():
            return print("Nenhum pagamento registrado ainda.")

        print("\n--- HISTÓRICO DE PAGAMENTOS (PIX) ---")
        for p in self.pagamentos.listar_todos():
            print(p)
        print("----------------------------------------\n")