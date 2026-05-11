vetor = []
pos = -1

for i in range(5):
    num = int(input("Digite um número: "))
    vetor.append(num)

x = int(input("Digite o valor que quer procurar: "))

for i in range(5):
    if vetor[i] == x:
        pos = i
        break

print(pos)