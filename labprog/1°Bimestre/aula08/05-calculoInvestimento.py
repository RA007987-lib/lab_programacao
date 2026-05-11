investimento_mensal=float(input("Quanto será investido por mês? R$"))
taxa_juros_mensal=float(input("Qual a taxa de juros mensal(1 para 1%)? "))/100
saldo = 0
ano_atual = 1
while True:
    # processamento mês a mês (1 ano = 12 interações)
    for mes in range(1, 13):
    # primeiro adiciona o aporte mensal ao saldo
     saldo +=investimento_mensal
    # depois aplique os juros sobre saldo acumulado
    saldo +=saldo*taxa_juros_mensal

    # saída do saldo após o ciclo de 12 meses
    print(f"\nSaldo do investimento após {ano_atual} ano (s): R$ {saldo:.2f}")
    # verificação se continua no próximo ano
    opcao=input("Deseja processar mais 1 ano?(S/N): ").upper()
    if opcao == 'S':
        ano_atual+=1
    else:
     print("Simulação encerrada")
     break

