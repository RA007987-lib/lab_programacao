numeros = []

for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

x = int(input("Digite o número X: "))

quantidade = numeros.count(x)

if quantidade > 0:
    indice = numeros.index(x)
    print(f"O número {x} aparece {quantidade} vez(es) na lista.")
    print(f"A primeira ocorrência está no índice {indice}.")
else:
    print(f"O número {x} não aparece na lista.")