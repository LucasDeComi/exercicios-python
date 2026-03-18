precoVeiculo = float(input("Insira o preço do veículo: "))
imposto = precoVeiculo * .45
lucro = (precoVeiculo + imposto) * .12
valorTotal = precoVeiculo + imposto + lucro
print("Preço do veículo: R$", precoVeiculo)
print("Valor em impostos: R$", imposto)
print("Lucro do vendedor: R$", lucro)
print("Valor total a ser pago: R$", valorTotal)