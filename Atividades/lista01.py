import random
lista1 = []
lista2 = [0, 0, 0, 0, 0, 0] #guardar contagem de cada face, no começo a face caiu 0 vezes, então vai ser [0,0,0,0,0,0]

lancamentos=[]
for i in range(100):
    resultado=random.randint(1,6)
    lancamentos.append(resultado)

frequencia = []
for face in range(1,7):
    quantidade = lancamentos.count(face)
    frequencia.append(quantidade)
print(lancamentos)
print("\nVetor de Frequências(Quantidade de vezes das faces: 1,2,3,4,5,6)")
print(frequencia)


