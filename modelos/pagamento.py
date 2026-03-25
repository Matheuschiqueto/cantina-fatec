from datetime import datetime

class Pagamento:
    """Modelo que representa um pagamento via PIX na cantina."""

    def __init__(self, nome, categoria, curso, valor):
        self.nome = nome
        self.categoria = categoria  
        self.curso = curso          
        self.valor = valor
        self.data_hora = datetime.now()

    def __str__(self):
        """Mostra recibo de pagamento."""
        data_formatada = self.data_hora.strftime("%d/%m/%Y %H:%M:%S")
        return f"[{data_formatada}] PIX de R$ {self.valor:.2f} | {self.nome} ({self.categoria} - {self.curso})"