# Cantina Fatec

Projeto desenvolvido para as disciplinas de Estrutura de Dados e Linguagem de Programação 2 da Fatec Rio Claro. 

O objetivo é construir um sistema de gestão para a cantina da Atlética, gerenciando estoque, pagamentos e consumo.

## TODO List (Roadmap)
- [x] Implementar classes base de Estrutura de Dados.
- [x] **Estoque:** Cadastro de produtos perecíveis (lógica FIFO/FEFO - prioridade para os mais velhos).
- [ ] **Pagamentos:** Registro de transações via PIX (separando por Aluno/Servidor/Professor e curso IA/ESG).
- [ ] **Vendas/Consumo:** Rotina para simular consumo, dar baixa no estoque e vincular ao pagamento.
- [ ] **Relatórios:** Criar extração de vendas e consumo.
- [ ] **Mock de Dados:** Gerar massa de testes com a lib `Faker`.
- [ ] **Persistência:** Salvar e carregar o estado da aplicação usando `pickle`.