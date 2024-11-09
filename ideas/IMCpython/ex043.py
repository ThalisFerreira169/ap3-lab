p = float(input("Digite seu peso(kg): "))
a = float(input("Digite sua altura(m): "))
imc = p / (a ** 2)
print("O IMC dessa pessoa é {:.1f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
elif imc >= 40:
    print("Obesidade mórbida")