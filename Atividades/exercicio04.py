notas = []

for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

menor_nota = min(notas)
notas.remove(menor_nota)

print("Notas restantes:")
for nota in notas:
    print(nota)