from RSA2 import *
from OAEP import oaep_encrypt, oaep_decrypt
import AES
import base64, hashlib

### PARTE I - GERAÇÃO DE CHAVES E CIFRAÇÃO ASSIMETRICA

qtdPrimos = 1000   # Qtd de primos para teste de Sieve Eratorthenes
sieveEratosthenes(qtdPrimos)

## Gera duas tuplas com as chaves públicas e privadas

# Gera p e q distintos
p = geradorPeQ() 
while True:
    q = geradorPeQ()
    if (p != q):
        break

print(f"P = {p}\n\n")
print(f"Q = {q}\n\n")

# 'n' e 'O(n)'
n = p * q
oDn = (p - 1) * (q - 1)

# Chaves públicas E e D
e = geraE(oDn)
d = geraD(e, oDn)

print(f"Suas chaves públicas são\n n = {n}\n e = {e}\n")
print(f"Suas chaves privadas são\n n = {n}\n d = {d}\n")

# Chaves em formato de tuplas
chavePublica = (e, n)
chavePrivada = (d, n)

msg = input("Digite a mensagem:\n")

#msg = open('texto.txt', 'r').read() 
#print('Conteúdo do arquivo:')
#print(msg)

c_key = AES.chvSess 
#Cifracao assimetrica da chave de sessao
c_key = oaep_encrypt(c_key)

print('Chave de sessao cifrada com RSA-OAEP')
print(c_key)

### PARTE II - ASSINATURA

### PARTE III

### PARTE IV