
# Sistema de Autenticação

# Define a senha correta
senha_correta = "1234"

# Inicializa o contador de tentativas
tentativas = 0

# Inicializa a variável de controlo
acesso = False

# Enquanto o utilizador não acertar e tiver menos de 3 erros
while tentativas < 3 and acesso == False:

    # Solicita a senha ao utilizador
    senha = input("Digite a sua senha: ")

    # Verifica se a senha está correta
    if senha == senha_correta:

        # Permite o acesso
        acesso = True
        print("Acesso autorizado! Bem-vindo.")

    else:

        # Conta mais uma tentativa incorreta
        tentativas = tentativas + 1

        # Informa quantas tentativas ainda restam
        print("Senha incorreta!")
        print("Tentativas restantes:", 3 - tentativas)

# Verifica se o utilizador foi bloqueado
if acesso == False:
    print("Acesso bloqueado! Número máximo de tentativas atingido.")
