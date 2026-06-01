nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

nomes_invertidos = nomes.copy()
nomes_invertidos.reverse()

print("Lista original:")
print(nomes)

print("Lista invertida:")
print(nomes_invertidos)