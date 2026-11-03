
# Análise de Números

# Cria uma lista vazia para guardar os números
numeros = []

# Utiliza o for para solicitar 5 números
for i in range(5):

    # Solicita um número ao utilizador
    numero = float(input(f"Digite o {i + 1}º número: "))

    # Adiciona o número à lista
    numeros.append(numero)

# Calcula a soma dos números
soma = sum(numeros)

# Calcula a média dos números
media = soma / 5

# Encontra o maior número
maior = max(numeros)

# Encontra o menor número
menor = min(numeros)

# Apresenta os resultados
print("\n===== RESULTADOS =====")
print("Soma:", soma)
print("Média:", media)
print("Maior número:", maior)
print("Menor número:", menor)
