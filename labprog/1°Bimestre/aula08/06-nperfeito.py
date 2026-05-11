n_desejado=int(input("Quantos números perfeitos você encontra? "))
encontrados = 0
numero_testado = 2 # começamos no 2 (1 não é perfeito )
print(f"Buscando os {n_desejado} primeiros numeros perfeitos")
while encontrados < n_desejado:
    soma_divisores = 0
     # encontra os divisores do 'número_testado'
    for i in range(1, numero_testado):
        if numero_testado % i == 0:
            soma_divisores += i

    # verificar se soma é igual ao número
    if soma_divisores == numero_testado:
        encontrados += 1
        print(f"{encontrados}. número perfeito encontrado: {numero_testado}")
    numero_testado += 1