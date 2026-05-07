#Escreva um programa Python que exiba na tela uma sequência de 10 números inteiros aleatórios entre 1 e 100.
import random

for num in range (1, 10 + 1):
    num = random.randint(1, 100)
    print (num)

