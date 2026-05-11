num = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
contador_pares = 0
while num <= num2:
    if(num%2 == 0):
      contador_pares += 1
    num = num + 1
    print(contador_pares)