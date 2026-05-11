print("="*30)
prova1 = int(input("Nota P1: "))
prova2 = int(input("Nota P2: "))
trabalho = int(input("Nota Trabalho: "))
participacao = int(input("Nota Participacao: "))
print("="*30)
# processamento
provas = 3*prova1 + 3*prova2
media = (provas + 3*trabalho + participacao)/10
# saida
print(f"MEDIA FOI DE {media}")