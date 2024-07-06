# Automação de Cadastro de Produtos com PyAutoGUI

Este projeto utiliza a biblioteca PyAutoGUI para automatizar o processo de cadastro de produtos em um sistema web. O script abre o navegador, realiza login no sistema e cadastra produtos a partir de uma base de dados em CSV.

## Requisitos

- Python 3.12
- Bibliotecas:
  - pyautogui
  - pandas

## Vantagens

- **Eficiência:** Automação do processo de cadastro, economizando tempo e esforço.
- **Precisão:** Minimiza erros humanos durante o preenchimento de formulários.
- **Facilidade de Uso:** Configuração simples e fácil execução.
- **Escalabilidade:** Pode ser adaptado para diferentes volumes de dados e requisitos de sistemas.
- **Flexibilidade:** Pode ser modificado para atender a diferentes interfaces e campos de entrada.

## Uso

1. Prepare a base de dados de produtos em um arquivo CSV (`produtos.csv`) no mesmo diretório do script, com a seguinte estrutura:

   | codigo | marca        | tipo        | categoria     | preco_unitario | custo | obs    |
   |--------|--------------|-------------|---------------|----------------|-------|--------|
   | 001    | Marca A      | Tipo 1      | Categoria X   | 100.0          | 50.0  | Promo  |
   | 002    | Marca B      | Tipo 2      | Categoria Y   | 150.0          | 75.0  | NaN    |

2. Execute o script:

```bash
python app.py

### Clonar o Repositório

```bash
git clone https://github.com/Arisson-Oliveira/Automation-Planilhas-Excel.git
cd Automation-Planilhas-Excel
