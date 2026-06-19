historico = []

while True:
    valor = float(input("Digite um valor (0 para sair): "))

    if valor == 0:
        break

    historico.append(valor)

for valor in historico[:]:
    if -5 < valor < 5:
        historico.remove(valor)

saldo = sum(historico)

print("Histórico restante:", historico)
print("Saldo final:", saldo)