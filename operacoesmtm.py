
# Menu de Operações Matemáticas

# Apresenta as opções disponíveis
print("===== MENU DE OPERAÇÕES =====")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Solicita a escolha do utilizador
opcao = int(input("Escolha uma operação: "))

# Solicita os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica a opção escolhida
match opcao:

    # Caso a opção seja 1, realiza a soma
    case 1:
        resultado = numero1 + numero2
        print("Resultado da soma:", resultado)

    # Caso a opção seja 2, realiza a subtração
    case 2:
        resultado = numero1 - numero2
        print("Resultado da subtração:", resultado)

    # Caso a opção seja 3, realiza a multiplicação
    case 3:
        resultado = numero1 * numero2
        print("Resultado da multiplicação:", resultado)

    # Caso a opção seja 4, realiza a divisão
    case 4:
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado da divisão:", resultado)
        else:
            print("Erro! Não é possível dividir por zero.")

    # Caso o utilizador escolha uma opção inválida
    case _:
        print("Opção inválida!")
