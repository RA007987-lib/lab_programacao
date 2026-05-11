n = int(input("Quantos valores você deseja inserir: "))
soma_quadrados = 0

for i in range(1, n+1):
    valor = float(input(f"Digite o {i} valor: "))
    # o quadrado pode ser valor*valor ou valor**2
    soma_quadrados += valor**2

print(f"\nA soma dos quadrados dos {n} valores é: {soma_quadrados:.2f}")