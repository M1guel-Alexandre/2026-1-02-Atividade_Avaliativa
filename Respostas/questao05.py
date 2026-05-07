#Escreva um programa que leia um número inteiro positivo repeticoes, depois leia repeticoes números inteiros e calcule: a soma total, a média, o maior valor, o menor valor, a quantidade de valores acima da média.

r = int(input("Digite a Quantidade de Números Inteiros que Deseja Adicionar: "))

soma = 0

for i in range (1, r + 1):
    numero = int(input(f"Digite {i}º número inteiro: "))
    soma = soma + numero
    maior = max(numero)
    menor = min(numero)
    
media = soma / r

print(f"A Soma dos números digitados é: {soma}")
print(f"a média dos valores é: {media}")
print(f"o maior valor é {maior}")
print(f"o menor valor é {menor}")
print(f"a quantidade de valores acima da média é {}")

