import random

vetor = []
cont = 0

for i in range(50):
    dado = random.randint(1, 6)
    vetor.append(dado)

    if dado == 6:
        cont += 1

percentual = (cont / 50) * 100

print("Quantidade de vezes que saiu 6:", cont)
print("Percentual:", percentual, "%")