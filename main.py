import os
from sistema.cantina import Cantina
from sistema.relatorios import Relatorios
from utils.gerador_dados import popular_cantina

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    minha_cantina = Cantina()
    
    if not minha_cantina.carregar_dados():
        print("Nenhum dado anterior encontrado.")
        resp = input("Deseja gerar 20 vendas aleatorias para teste agora? (s/n): ")
        if resp.lower() == 's':
            popular_cantina(minha_cantina, qtd_vendas=20)
            input("\nPressione Enter para continuar para o menu...")

    relatorios = Relatorios(minha_cantina)

    while True:
        limpar_tela()

        print("\n--- SISTEMA CANTINA FATEC ---")
        print("1. Ver Estoque")
        print("2. Realizar Venda Manual")
        print("3. Ver Relatorios e Consumo")
        print("4. Gerar dados de teste (Faker)")
        print("0. Sair e Salvar")
        
        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":
            minha_cantina.estoque.listar_estoque()
        
        elif opcao == "2":
            nome = input("Nome do Cliente: ")
            cat = input("Categoria (Aluno/Professor/Servidor): ")
            curso = input("Curso (IA/ESG/Nenhum): ")
            prod = input("Produto: ")
            
            qtd_str = input("Quantidade: ")
            if qtd_str.isdigit():
                qtd = int(qtd_str)
                minha_cantina.realizar_venda(nome, cat, curso, prod, qtd)
            else:
                print("Quantidade invalida.")

        elif opcao == "3":
            relatorios.gerar_resumo_financeiro()
            relatorios.faturamento_por_categoria()
            relatorios.faturamento_por_curso()
            relatorios.relatorio_consumo_produtos()
            relatorios.extrato_detalhado_vendas()

        elif opcao == "4":
            qtd_str = input("Quantas vendas deseja simular? ")
            if qtd_str.isdigit():
                popular_cantina(minha_cantina, qtd_vendas=int(qtd_str))
                print(f"Sucesso: {qtd_str} vendas geradas.")
            else:
                print("Numero invalido.")

        elif opcao == "0":
            minha_cantina.salvar_dados()
            print("Encerrando sistema e salvando dados...")
            break
        else:
            print("Opcao invalida.")

        if opcao in ["1", "2", "3", "4"]:
            input("\nPressione Enter para voltar ao menu...")

if __name__ == "__main__":
    menu()