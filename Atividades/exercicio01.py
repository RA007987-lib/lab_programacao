vetor = []
diferentes = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

for i in range(10):
    repetido = False

    for j in range(i):
        if vetor[i] == vetor[j]:
            repetido = True

    if repetido == False:
        diferentes += 1

print("Quantidade de valores diferentes:", diferentes)