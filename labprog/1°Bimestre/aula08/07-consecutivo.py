num=int(input("Digite um número para verificar se é produto de 3 consecutivos"))
triangular=False
i= 1
# testando enquanto o produto for menor ou igual a n 
while i * (i+1)*(i+2) <= num :
    if i * (i+1)*(i+2)==num :
        print(f"Sim! {num} é o produto de {i}x{i+1}x{i+2}")
        triangular = True
        break
    i +=1

    if not triangular:
        print(f"O número {num} NÃO é produto de 3 inteiros consecutivos.")