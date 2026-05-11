# 1. Entrada de Dados
print("--- CALCULADORA DE IMC ---")
massa = float(input("Informe o peso (kg): "))
altura = float(input("Informe a altura (m): "))               

# 2. Processamento: IMC = massa / altura*
# Em Python, a potência é feita com **
imc = massa / (altura ** 2 )

# 3. Classificação (Lógica IF-ELIF-ELSE)
if imc <18.5:
    classificacao = "Abaixo do peso"
elif imc <= 24.9:
    classificacao = "Saudável"
elif imc <= 29.9: 
    classificacao = "Peso em execesso"
elif imc <= 34.9:
    classificacao = "Obesidade Grau I"
elif imc <= 39.9:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III"

# 4. Saída de dados:
print("-" * 30)
print(f"SEU IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")   