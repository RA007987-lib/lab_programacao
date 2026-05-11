 # Quero saber a media da nota do aluno
nome1 = input("Nome aluno 1: ")
nome2 = input("Nome aluno 2: ")
nome3 = input("Nome aluno 3: ")
nota1 = float(input(f"nota de {nome1}: "))
nota2 = float(input(f"nota de {nome2}: "))
nota3 = float(input(f"nota de {nome3}: "))
media = (nota1 + nota2 + nota3)/3
print(f"A média da turma é {media:.2f}")
if nota1>media:
    print(f"Parábens {nome1}, sua nota {nota1}")
if nota2>media:
    print(f"Parábens {nome2}, sua nota {nota2}")
if nota3>media:
    print(f"Parábens {nome3}, sua nota {nota3}")
