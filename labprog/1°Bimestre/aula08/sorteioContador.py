import random
x = int(input("Digite um número entre 1 e 10: "))
soma = 0 
contador = 0
while contador <= x :
    numero_sorteado = random.randint(1,10)
    print(numero_sorteado)
    soma = soma + numero_sorteado
    contador = contador + 1
    print(numero_sorteado)
print("A soma é ",soma)