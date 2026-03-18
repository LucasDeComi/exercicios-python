vendedorID = int(input("Qual o código do vendedor? "))
codPeca = int(input("Qual o código do peça? "))
valorPeca = float(input("Qual o valor unitário da peça? "))
qtd = int(input("Quantas peças foram vendidas? "))
comissao = (valorPeca * qtd) * 0.05

print("O vendedor de código ", vendedorID, " vendeu ", qtd, " peças de codigo ", codPeca,", ganhando uma comissão de: ", comissao)