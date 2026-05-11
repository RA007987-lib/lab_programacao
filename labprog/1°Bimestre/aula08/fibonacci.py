n_termos = int(input("Quantos termos da série de fibonacci deseja ver ?"))
a, b = 0,1
contador = 0
print("Sequência de fibonacci")
while contador <= n_termos:
    print(a,end=", " if contador < n_termos else "")
    #lógica ede atualização F(n) = F(n-1)+ F(n-2)
    proximo = a + b # 1
    a = b # 1
    b = proximo # 1
    contador +=1 