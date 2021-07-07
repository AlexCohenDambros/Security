matrizCredenciais = [["vilmar", "123456", 0], ["junior", "abcdef", 0]]

loop = True
while( loop ):

    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

    for credencial in matrizCredenciais:
        usuarioCorrente = credencial[0]
        senhaCorrente = credencial[1]
        tentativas = credencial[2]

        if usuario == usuarioCorrente and senha == senhaCorrente:
            if( tentativas < 5 ):
                credencial[2] = 0
                loop = False
            else:
                print("Usuario esta bloqueado, contate o administrador!")
        elif usuario == usuarioCorrente:
            credencial[2] = tentativas + 1
            if (credencial[2] >= 5):
                print("Usuario foi bloqueado!")


    if loop == True:
        print("Usuario ou senha invalido!")
    else:
        print("Usuario autenticado com sucesso!")

