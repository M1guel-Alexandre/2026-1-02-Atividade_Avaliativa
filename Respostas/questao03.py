#Escreva um programa que recebe um inteiro positivo numero e determina se numero é um número perfeito (um número é perfeito se a soma de seus divisores próprios é igual a ele mesmo, ex: 6 = 1+2+

numero = int(input("Digite um Número: "))
soma = 0

for divisor in range(1, numero):
    if numero % divisor == 0:
        soma += divisor

if soma == numero:
    print(f"O {numero} é Perfeito")
else:
    print(f"O {numero} é Imperfeito")
