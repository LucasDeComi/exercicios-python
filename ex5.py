nome = input("Qual o seu nome? ")
salario = float(input("Qual o seu salário atual? "))
salarioNovo = 0.0
if salario <= 1000:
    salarioNovo = salario * 1.2
elif salario <= 5000:
    salarioNovo = salario * 1.1
else:
    salarioNovo = salario * 1.05
print("Nome do jogador: ", nome)
print("Salário reajustado: ", salarioNovo)