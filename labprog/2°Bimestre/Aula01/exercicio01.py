vetor = []
cont = 0

for i in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)

for i in range(10):
    igual = False

    for j in range(i):
        if vetor[i] == vetor[j]:
            igual = True

    if igual == False:
        cont += 1

print("Valores diferentes:", cont)