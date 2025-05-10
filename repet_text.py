# Recebe a string e o número de repetições
texto = input("Digite a string que deseja repetir: ")
repeticoes = int(input("Digite o número de repetições: "))

# Adiciona espaço entre as repetições
resultado = (texto + " ") * repeticoes

# Remove o último espaço extra
resultado = resultado.strip()

# Exibe o resultado
print("Resultado da repetição:", resultado)
