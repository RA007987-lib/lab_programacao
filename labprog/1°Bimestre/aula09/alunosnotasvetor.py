qtde_alunos = 2
nomes = []
notas = []
media = 0
for i in range(qtde_alunos):
    nomes.append(input(f"Nome do aluno {i+1}: "))
    notas.append(float(input(f"Nota de {nomes [i]}: ")))
    media = media + notas[i]

media = media / qtde_alunos
print(f"\nA média da turma é {media:.2f}.\n")

print("Alunos com notas a cima da média: ")
for i in range(qtde_alunos):
    if notas[i] > media:
        print(f"Parabéns {nomes[i]}! Sua nota foi {notas[i]:.1f}")

print(nomes,notas)