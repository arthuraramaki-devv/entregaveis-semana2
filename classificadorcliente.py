# Classificador de Cliente

# Solicita a idade do cliente
idade = int(input("Digite a sua idade: "))

# Solicita a renda mensal do cliente
renda = float(input("Digite a sua renda mensal: "))

# Verifica a idade e a renda para classificar o cliente
if idade < 18:
    print("Cliente não elegível para classificação.")

elif renda < 1500:
    print("Categoria: Bronze")

elif renda < 3000:
    print("Categoria: Prata")

elif renda < 6000:
    print("Categoria: Ouro")

else:
    print("Categoria: Diamante")
