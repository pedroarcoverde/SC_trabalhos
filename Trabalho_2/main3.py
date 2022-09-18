#!/usr/bin/python3

import base64
import secrets
from pathlib import Path

import RSA3
import AES


op = 0
while(op != 4):
    op = int(input("ESCOLHA UMA OPÇÃO:\n\n1) GERAR CHAVES\n2) CIFRAR\n3) DECIFRAR\n4) FECHAR\n"))

    # GERA AS CHAVES PÚBLICAS E PRIVADAS
    if op == 1:
        chave_publica, chave_privada = RSA3.gera_chaves()

        print(chave_publica)
        print()
        print(chave_privada)
        print()

    # CIFRA E ASSINA A MSG
    elif op == 2:
        secrets.token_bytes(16), secrets.token_bytes(16)
        chave, iv = secrets.token_bytes(16), secrets.token_bytes(16)

        chave_sess = chave + iv
        chave_sess_cifra = RSA3.cifra(chave_publica, chave_sess)
        chave_sess_cifra = base64.b64encode(chave_sess_cifra).decode("ascii")

        with open(Path(__file__).absolute().parent / "texto.txt", "rb") as file: # Leitura do arquivo "texto.txt"
            msg = file.read()
        msg_cifrada = AES.ctr(msg, chave, iv)

        assinatura = RSA3.assina(chave_privada, msg)
        assinatura = base64.b64encode(assinatura).decode("ascii")

        print('MENSAGEM:\n')
        print(msg)
        print('\nMENSAGEM CIFRADA:\n')
        print(msg_cifrada)
        print('\nCHAVE DA SESSÃO:\n')
        print(chave_sess)
        print('\nCHAVE DA SESSÃO DA CIFRA:\n')
        print(chave_sess_cifra)
        print()

    # DECIFRA E VERIFICA ASSINATURA DA CIFRA
    elif op == 3:
       
        assinatura = base64.b64decode(assinatura)
        chave_sess_cifra = base64.b64decode(chave_sess_cifra)
        
        chave_sess = RSA3.decifra(chave_privada, chave_sess_cifra)
        chave, iv = chave_sess[:16], chave_sess[16:]

        msg = AES.ctr(msg_cifrada, chave, iv)
        confere = RSA3.verifica_assinatura(chave_publica, msg, assinatura)

        if confere:
            print("Assinatura confere")
            print('MENSAGEM:\n')
            print(msg)
            #with open('texto.txt', "wb") as f:
            #    f.write(msg)
        else:
            print("Assinatura NÃO confere")



    # ENCERRA O PROGRAMA
    elif op == 4:
        break

    else:
        continue

