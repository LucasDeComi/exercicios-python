nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print("Média do aluno: ", media)

if media >= 8:
    print("Conceito: A")
elif media >= 5:
    print("Conceito: B")
else:
    print("Conceito: C")