# Vamos criar uma calculadora de operações matemáticas simples.
# O usuário irá informar dois números e a operação que deseja realizar (soma, subtração, multiplicação ou divisão).
# O programa deverá exibir o resultado da operação.

# Recebendo os dados do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja realizar (soma, subtração, multiplicação ou divisão): ")

# Realizando a operação
if operacao == "soma":
    resultado = numero1 + numero2
elif operacao == "subtração":
    resultado = numero1 - numero2
elif operacao == "multiplicação":
    resultado = numero1 * numero2
elif operacao == "divisão":
    resultado = numero1 / numero2
else:
    resultado = "Operação inválida"

# Exibindo o resultado
print("O resultado da operação é: ", resultado)
