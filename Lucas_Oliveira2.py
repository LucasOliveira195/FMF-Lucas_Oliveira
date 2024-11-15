peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibe o resultado
print(f"O seu IMC é: {imc:.2f}")

# Interpretação do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc <= 24.9:
    print("Você está com peso normal.")
elif 25 <= imc <= 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
