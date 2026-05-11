num = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = 0 
for i in range(num,num2 + 1):
    if(i%2 == 0):
      soma = soma + i 
    print("A soma é ", soma)