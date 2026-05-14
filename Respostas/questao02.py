#Escreva um programa Python que leia um número inteiro positivo e armazene na variável repeticoes; e exiba na tela uma sequência de repeticoes números inteiros aleatórios entre 1 e 100.

import random

numero = int(input("Digite um número: "))
for num in range (1, numero + 1):
    num = random.randint(1, 100)
    print (num)