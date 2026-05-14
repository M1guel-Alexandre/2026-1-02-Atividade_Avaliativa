#Escreva um programa que leia um número inteiro positivo repeticoes, depois leia repeticoes números inteiros e calcule: a soma total, a média, o maior valor, o menor valor, a quantidade de valores acima da média.

repetições = int(input("Digite a Quantidade de Números Inteiros que Deseja Adicionar: "))
numeros = []
soma = 0
maior = -1
menor = 9999999999
acima = 0

for i in range (1, repetições + 1):
    numero = int(input(f"Digite {i}º número inteiro: "))
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:  
        menor = numero
    numeros.append(numero)


media = soma / repetições

for numero in numeros:
    if numero > media:
        acima += 1

print(f"A Soma dos números digitados é: {soma}")
print(f"a média dos valores é: {media}")
print(f"o maior valor é {maior}")
print(f"o menor valor é {menor}")
print(f"a quantidade de valores acima da média é {acima}")

