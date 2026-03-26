class Relatorios:
    """Classe responsável por processar os dados e gerar estatísticas da cantina."""

    def __init__(self, cantina):
        # Recebe o objeto cantina inteiro para acessar estoque e histórico
        self.cantina = cantina
        self.historico = cantina.historico

    def gerar_resumo_financeiro(self):
        """Calcula o faturamento total e quantidade de vendas."""
        pagamentos = self.historico.pagamentos.listar_todos()
        total_faturado = sum(p.valor for p in pagamentos)

        print("\n" + "="*40)
        print(f"{'RESUMO FINANCEIRO GERAL':^40}")
        print("="*40)
        print(f"Total Arrecadado (PIX): R$ {total_faturado:.2f}")
        print(f"Total de Transações: {len(pagamentos)}")
        print("="*40 + "\n")

    def faturamento_por_categoria(self):
        """Agrupa quanto Alunos, Professores e Servidores gastaram."""
        resumo = {"Aluno": 0.0, "Professor": 0.0, "Servidor": 0.0}
        for p in self.historico.pagamentos.listar_todos():
            if p.categoria in resumo:
                resumo[p.categoria] += p.valor

        print("--- FATURAMENTO POR CATEGORIA ---")
        for cat, valor in resumo.items():
            print(f" {cat:.<15}: R$ {valor:>8.2f}")
        print("-" * 36 + "\n")

    def faturamento_por_curso(self):
        """Agrupa vendas por IA vs ESG."""
        resumo = {"IA": 0.0, "ESG": 0.0, "Nenhum": 0.0}
        for p in self.historico.pagamentos.listar_todos():
            if p.curso in resumo:
                resumo[p.curso] += p.valor

        print("--- FATURAMENTO POR CURSO ---")
        for curso, valor in resumo.items():
            print(f" {curso:.<15}: R$ {valor:>8.2f}")
        print("-" * 32 + "\n")

    def relatorio_consumo_produtos(self):
        """Relatório de Consumo: Ranking de itens mais vendidos."""
        consumo = {}
        
        for p in self.historico.pagamentos.listar_todos():
            if p.produto in consumo:
                consumo[p.produto] += p.quantidade
            else:
                consumo[p.produto] = p.quantidade

        print("--- RANKING DE CONSUMO (PRODUTOS) ---")
        # Ordena do mais vendido para o menos vendido
        ranking = sorted(consumo.items(), key=lambda item: item[1], reverse=True)
        
        for prod, qtd in ranking:
            print(f" {prod:.<20}: {qtd} unidades")
        print("-" * 40 + "\n")

    def extrato_detalhado_vendas(self):
        """Mostra a lista de todas as vendas realizadas (Extrato)."""
        print("--- EXTRATO DETALHADO DE VENDAS ---")
        self.historico.listar_pagamentos()
        print("-" * 40 + "\n")