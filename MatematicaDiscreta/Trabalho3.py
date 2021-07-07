# Descrição 1

banco = {'A': '11000',
         'B': '10011',
         'C': '01110',
         'D': '10010',
         'E': '10000',
         'F': '10110',
         'G': '01011',
         'H': '00101',
         'I': '01100',
         'J': '11010',
         'K': '11110',
         'L': '01001',
         'M': '00111',
         'N': '00110',
         'O': '00011',
         'P': '01101',
         'Q': '11101',
         'R': '01010',
         'S': '10100',
         'T': '00001',
         'U': '11100',
         'V': '01111',
         'W': '11001',
         'X': '10111',
         'Y': '10101',
         'Z': '10001',
         '9': '00100',
         '8': '11111',
         '+': '11011',
         '4': '01000',
         '3': '00010',
         '/': '00000'}


def cripto():
    global x

    print("=================================")
    entradaChave = input("Entre com a chave: ")
    entradaPalavra = input("Entre com a palavra para ser criptografada: ")

    entradaChave = entradaChave.upper()
    listaC = list(entradaChave)

    entradaPalavra = entradaPalavra.upper()
    lista = list(entradaPalavra)

    listaAAA = []
    for y in range(len(lista)):
        try:
            try:
                listaAAA.append(listaC[y])
                y += 1
            except:
                listaAAA.append(listaC[x])
                x += 1
        except:
            x = 0
            listaAAA.append(listaC[x])
            x += 1

    print("resposta: ", end='')
    for l in range(len(lista)):
        try:
            try:
                var1 = banco[lista[l]]
            except:
                if lista[l] == ' ':
                    var1 = banco['9']
                elif lista[l] == '.':
                    var1 = banco['+']
                elif lista[l] == '?':
                    var1 = banco['8']
                elif lista[l] == ',':
                    var1 = banco['3']
                elif lista[l] == '!':
                    var1 = banco['4']
                elif lista[l] == ';':
                    var1 = banco['/']
        except:
            print("falhou / caractere nao identificado")

        try:
            try:
                var2 = banco[listaAAA[l]]
            except:
                if listaAAA[l] == ' ':
                    var2 = banco['9']
                elif listaAAA[l] == '.':
                    var2 = banco['+']
                elif listaAAA[l] == '?':
                    var2 = banco['8']
                elif listaAAA[l] == ',':
                    var2 = banco['3']
                elif listaAAA[l] == '!':
                    var2 = banco['4']
                elif listaAAA[l] == ';':
                    var2 = banco['/']

        except:
           print("falhou / caractere nao identificado")

        try:
            var1 = int(var1, 2)
            var2 = int(var2, 2)
            varFinal = var1 ^ var2
            varFinal = '{0:05b}'.format(varFinal)
            print(get_key(varFinal), end='')
        except:
            print("Alguns dos caracteres inseridos nao estão na base de dados")
            break




def get_key(val):
    for key, value in banco.items():
        if val == value:
            return key

    return "Essa chave não existe"


def descripto():
    print("=================================")
    entradaChave = input("Entre com a chave: ")
    entradaCifra = input("Entre com o texto criptografado: ")

    entradaChave = entradaChave.upper()
    listaChave = list(entradaChave)

    entradaCifra = entradaCifra.upper()
    listaCifra = list(entradaCifra)

    listaAAA = []

    print("resposta: ", end='')
    for y in range(len(listaCifra)):
        try:
            try:
                listaAAA.append(listaChave[y])
                y += 1
            except:
                listaAAA.append(listaChave[x])
                x += 1

        except:
            x = 0
            listaAAA.append(listaChave[x])
            x += 1

    for l in range(len(listaCifra)):
        try:
            try:
                var1 = banco[listaCifra[l]]
            except:
                if listaCifra[l] == ' ':
                    var1 = banco['9']
                elif listaCifra[l] == '.':
                    var1 = banco['+']
                elif listaCifra[l] == '?':
                    var1 = banco['8']
                elif listaCifra[l] == ',':
                    var1 = banco['3']
                elif listaCifra[l] == '!':
                    var1 = banco['4']
                elif listaCifra[l] == ';':
                    var1 = banco['/']
        except:
            print("falhou / caractere nao identificado")

        try:
            try:
                var2 = banco[listaAAA[l]]
            except:
                if listaAAA[l] == ' ':
                    var2 = banco['9']
                elif listaAAA[l] == '.':
                    var2 = banco['+']
                elif listaAAA[l] == '?':
                    var2 = banco['8']
                elif listaAAA[l] == ',':
                    var2 = banco['3']
                elif listaAAA[l] == '!':
                    var2 = banco['4']
                elif listaAAA[l] == ';':
                    var2 = banco['/']

        except:
            print("falhou / caractere nao identificado")

        try:
            var1 = int(var1, 2)
            var2 = int(var2, 2)
            varFinal = var1 ^ var2
            varFinal = '{0:05b}'.format(varFinal)
            print(get_key(varFinal), end='')
        except:
            print("Alguns dos caracteres inseridos nao estão na base de dados")
            break


options = {'1': cripto,
           '2': descripto}
loop = True
while loop:
    escolhaMenuPrincipal = input("\n================================= \n"
                                 '1 - Criptografar. \n'
                                 '2 - Descriptografar. \n'
                                 '3 - Sair. \n'
                                 "Escolha uma opção: ")

    if escolhaMenuPrincipal == '3':
        break

    func = options.get(escolhaMenuPrincipal, lambda: 'Opção Inválida!\n')

    if func == cripto:
        func()

    if func == descripto:
        func()
