# Vamos receber um texto do usuário  e um número. Depois iremos repetir o texto pela quantidade do número recebido .

# Recebendo os dados do usuário
texto = input("Digite um texto: ")
numero = int(input("Digite um número: "))
# Repetindo o texto
texto_repetido = texto * numero
# Exibindo o resultado
print("O resultado é: ", texto_repetido)
