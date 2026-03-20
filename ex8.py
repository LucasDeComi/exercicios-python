soma = 0
for i in range(1, 6):
    # f antes da string funciona como uma forma de concatenação
    num = int(input(f"Digite o {i}º número: "))
    soma += num
print("Soma total: ", soma)