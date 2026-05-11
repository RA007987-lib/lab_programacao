# 1 - Definição da constante fisica (Velocidade do som em m/s)
velocidade_som = 340

# entrada
# 2 - leia tempo - Tempo em segundos
tempo = float(input("Digite o tempo entre o clarão e o trovão(em segundos): ")) #8

# 3 - processamento
# distância em metros = velocidade * tempo
distanciaMetros = velocidade_som * tempo # 2720 metros

# convertendo para quilometros
distanciaKm = distanciaMetros / 1000

# 4 - saida de dados
print(f"O raio caiu a uma distância aproximada de {distanciaKm:.2f} km")
