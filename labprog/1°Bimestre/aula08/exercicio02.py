num = int(input('Digite um número: '))
contador = 0
if num ==0:
    contador = 1
else:
    temp = num 
    while temp > 0:
        temp //=10 # remove o último dígito 
        contador +=1

print(f"O número {num} possui {contador} digitos.")