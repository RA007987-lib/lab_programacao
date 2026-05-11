# Entrada do valor em centavos .
valor = int(input("Digite o valor em centavos: "))
print(f"Para o valor {valor} centavos,a menor quantidades de moedas é:")
# calculo para moedas de 1 real(100 centavos)
moedas1real = valor //100
valor = valor % 100 
# cálculo para moedas de 50 cents.
moedas50 = valor // 50
valor = valor % 50
# cálculo para moedas de 25 cents.
moedas25 = valor // 25
valor = valor % 25
# cálculo para moedas de 10 cents.
moedas10 = valor // 10
valor = valor % 10
# cálculo para moedas de 5 cents.
moedas5 = valor // 5
valor = valor % 5
#cálculo para moedas de 1 cents.
moedas1 = valor // 1
valor = valor % 1
 
 # Exibição dos resultados (Apenas maior que 0)
if moedas1real > 0:
    print(f"-{moedas1real} moeda(s) de 1 real")
if moedas50 > 0:
    print(f"-{moedas50} moeda(s) de 50 centavos")
if moedas25 > 0: 
     print(f"-{moedas25} moeda(s) de 25 centavos")
if moedas10 > 0:
     print(f"-{moedas10} moeda(s) de 10 centavos")
if moedas5 > 0:
       print(f"-{moedas5} moeda(s) de 5 centavos")
if moedas1 > 0:
       print(f"-{moedas1} moeda(s) de 1 centavos")