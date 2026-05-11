import random

vetor = []
cont = 0

for i in range(50):
    numero = random.randint(1, 6)
    vetor.append(numero)

    if numero == 6:
        cont += 1

porcentagem = (cont * 100) / 50

print("Face 6 apareceu", cont, "vezes")
print("Porcentagem:", porcentagem, "%")