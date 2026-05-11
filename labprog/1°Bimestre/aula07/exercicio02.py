# entrada
Nivel= int(input("informe o nivel atual do reservatorio (%):"))

#processamento
if Nivel >=90:
    status = "Nivel Crítico(Transbordamento)!"
elif Nivel >=50:
    status = "Nivel Adequado."
elif Nivel >=20:
    status = "Nivel baixo (Atenção)"
else:
    status = " PERIGO: Nível mínimo atingido!"

print(f"Status do sistema: {status}")