vetor = []

for i in range(5):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

x = int(input("Digite o valor que deseja procurar: "))

posicao = -1

for i in range(5):
    if vetor[i] == x:
        posicao = i
        break

print("Posição:", posicao)