# Solicita os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicita a operação a ser realizada
operacao = input("Digite a operação (+, -, *, /): ")

# Realiza a operação escolhida e aplica o valor absoluto (abs)
if operacao == "+":
    resultado = abs(numero1 + numero2)
elif operacao == "-":
    resultado = abs(numero1 - numero2)
elif operacao == "*":
    resultado = abs(numero1 * numero2)
elif operacao == "/":
    if numero2 != 0:
        resultado = abs(numero1 / numero2)
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print(f"Resultado: {resultado}")
