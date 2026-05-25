notas=[2.5,7.5,10.0,4.0] #Vetor

soma=0

for nota in notas:
    soma+=nota #soma= soma+nota (0+2.5+4.0....)
media=soma/len(notas)

proximo_media = notas[0]
menor_distancia = abs(notas[0] - media)
for nota in notas:
    dist_atual = abs(nota - media)
    if dist_atual < menor_distancia:
        menor_distancia = dist_atual
        proximo_media = nota


print(f"Vetor: {notas}")
print(f"Média: {media:.1f}")
print(f"Mais próximo da média: {proximo_media}")
