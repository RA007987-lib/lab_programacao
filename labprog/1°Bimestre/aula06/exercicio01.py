"""Leia VALOR_PRODUTO
    DESCONTO ← VALOR_PRODUTO * 0.15
    PRECO_FINAL ← VALOR_PRODUTO - DESCONTO
    Escreva "Desconto: R$", DESCONTO
    Escreva "Total a pagar: R$", PRECO_FINAL
"""
valor_produto = float(input("Valor do Produto: "))
desconto = valor_produto * 0.15
preco_final = valor_produto - desconto
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {preco_final:.2f}")