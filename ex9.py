peso = float(input("Insira o seu peso: "))
altura = float(input("Insira a sua altura: "))

imc = peso / (altura ** 2)
print("Seu IMC é: ",imc)
if imc < 18.5:
    print("Você está abaixo do peso ideal")
elif imc < 25:
    print("Você está no peso ideal")
elif imc < 30:
    print("Você está acima do peso ideal")
elif imc < 35:
    print("Você está no grau de obesidade I")
elif imc < 40:
    print("Você está no grau de obesidade II")
else:
    print("Você está no grau de obesidade III")