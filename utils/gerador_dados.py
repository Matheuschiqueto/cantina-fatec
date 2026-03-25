import random
from faker import Faker
from modelos.produto import Produto

def popular_cantina(cantina, qtd_vendas=20):
    """
    Usa o Faker para gerar um estoque inicial e simular dezenas de vendas aleatórias.
    """
    fake = Faker('pt_BR')
    
    print("\nIniciando simulação de dados com Faker...")

    nomes_produtos = ["Coxinha", "Kibe", "Suco", "Refrigerante", "Bolo de Cenoura"]
    
    print("Abastecendo as prateleiras...")
    for nome in nomes_produtos:
        for _ in range(random.randint(1, 3)):
            data_compra = fake.date_between(start_date='-30d', end_date='today').strftime("%Y-%m-%d")
            
            data_venc = fake.date_between(start_date='today', end_date='+30d').strftime("%Y-%m-%d")
            
            preco_custo = round(random.uniform(2.0, 5.0), 2)
            preco_venda = preco_custo * 2.0 
            qtd = random.randint(15, 40)
           
            lote = Produto(nome, preco_custo, preco_venda, data_compra, data_venc, qtd)
            cantina.estoque.cadastrar_produto(lote)

    print(f"\n Simulando {qtd_vendas} vendas com alunos e professores...")
    categorias = ["Aluno", "Professor", "Servidor"]
    cursos = ["IA", "ESG"]

    for _ in range(qtd_vendas):
        nome_cliente = fake.name() 
        categoria = random.choice(categorias)
        
        curso = random.choice(cursos) if categoria != "Servidor" else "Nenhum"
        
        produto_escolhido = random.choice(nomes_produtos)
        qtd_comprada = random.randint(1, 3)

        cantina.realizar_venda(nome_cliente, categoria, curso, produto_escolhido, qtd_comprada)
        
    print("\n Simulação concluída com sucesso!")