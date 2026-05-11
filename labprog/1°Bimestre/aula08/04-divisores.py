while True:
    num=int(input("\nDigite um número inteiro positivo: "))
    # conta divisores
    qtde_divisores = 0
    print(f"Divisores de {num}: ",end="")
    #loop para encontrar e exibir os divisores
    for i in range(1,num+1):
        if num%i==0:
            print(i, end=" ") # exibi os divisores
            qtde_divisores +=1

    # Verificar se o número é primo baseado na qtde
    print()
    if qtde_divisores == 2:
        print(f"Conclusão: O número {num} é PRIMO")
    else:
        print(f"Conclusão: O número {num} NÃO é primo (possui {qtde_divisores} divisores)")
    
    # opção para inserir novo número
    continuar=input("\nDeseja analisar outro número?(S/N): ").upper()
    if continuar != 'S':
        break 