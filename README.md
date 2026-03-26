# Cantina Fatec

Projeto desenvolvido para as disciplinas de Estrutura de Dados e Linguagem de Programação 2 da Fatec Rio Claro. 

O objetivo é construir um sistema de gestão para a cantina da Atlética, gerenciando estoque, pagamentos e consumo.

## Funcionalidades Implementadas

- [x] Implementar classes base de Estrutura de Dados.
- [x] **Estoque:** Cadastro de produtos perecíveis (lógica FIFO/FEFO - prioridade para os mais velhos).
- [x] **Pagamentos:** Registro de transações via PIX (separando por Aluno/Servidor/Professor e curso IA/ESG).
- [x] **Vendas/Consumo:** Rotina para simular consumo, dar baixa no estoque e vincular ao pagamento.
- [x] **Relatórios:** Criar extração de vendas e consumo.
- [x] **Mock de Dados:** Gerar massa de testes com a lib `Faker`.
- [x] **Persistência:** Salvar e carregar o estado da aplicação usando `pickle`.

## Requisitos

- Python 3.8+
- Bibliotecas: `faker`

## Como Executar

1. Crie um ambiente virtual:
```bash
python -m venv venv
```

2. Ative o ambiente virtual:
```bash
# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
python main.py
```

5. Interaja com o menu interativo para:
   - Adicionar/remover produtos do estoque
   - Registrar pagamentos
   - Simular vendas
   - Gerar relatórios
   - Persistir dados

## Estrutura do Projeto

```
cantina-fatec/
├── main.py                    # Arquivo principal com menu interativo
├── requirements.txt           # Dependências do projeto
├── README.md                  # Este arquivo
├── estruturas/                # Implementação de estruturas de dados
│   ├── fila.py               # Implementação da Fila
│   └── lista.py              # Implementação da Lista
├── modelos/                   # Modelos de dados
│   ├── pagamento.py          # Modelo de Pagamento
│   └── produto.py            # Modelo de Produto
├── sistema/                   # Lógica principal do sistema
│   ├── cantina.py            # Gerenciador central da cantina
│   ├── estoque.py            # Gerenciamento de estoque
│   ├── historico_pagamento.py # Histórico de transações
│   └── relatorios.py         # Geração de relatórios
└── utils/                     # Utilitários
    └── gerador_dados.py      # Gerador de dados mock com Faker
```

## Persistência de Dados

O sistema utiliza `pickle` para salvar e carregar o estado completo da aplicação, permitindo:
- Manutenção de dados entre execuções
- Recuperação de histórico de transações
- Backup automático do estado da cantina

## Relatórios Disponíveis

- Resumo de estoque
- Histórico de vendas
- Análise de pagamentos por categoria (Aluno/Servidor/Professor)
- Análise por curso (IA/ESG)
- Movimentação de produtos (entrada/saída)