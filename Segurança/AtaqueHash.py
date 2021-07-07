import time
import hashlib
import itertools
import string

#Este programa ele quebra chaves de 4 caracteres, se quiser mudar eh so alterar os dados no (for password_length in range(4, 4):) os valores no range!!!
#Também está falantando alguns caracteres especiais, apenas alguns estão inclusos!!

usuarios_cadastrados = dict()


def guess_password(real):
    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + "<>?=_.,;:çÇ~´[!@#$\%¨&*()*-+/"
    attempts = 0
    for password_length in range(3, 5):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)

            md5Guess = hashlib.md5(guess.encode('utf-8')).hexdigest()

            if md5Guess == real:
                return 'senha é {}. encontrado em {} tentativas.'.format(guess, attempts)


f = open("../Projeto/senhasgravadas.txt", "r")
fr = f.read().splitlines()
for line in fr:
    (key, val) = line.split(";")
    usuarios_cadastrados[key] = val

for usuario in usuarios_cadastrados:
    start = time.time()
    print("Usuario: " + str(usuario))
    print("Hash: " + usuarios_cadastrados.get(usuario))
    print("Senha: ", guess_password(usuarios_cadastrados.get(usuario)))
    end = time.time()
    total = end-start
    print("Tempo: " + str(total) + "s")
    print("=================================")