frase = ("Digite uma frase: ( ex:Aula 01 de SQL)")

conta_letras=0
conta_numeros=0
for caractere in frase:
    if caractere.isalpha():
        conta_letras +=1
    elif caractere.isdigit():
        conta_numeros +=1

print(f"Na sua frase existem {conta_letras} letras e {conta_numeros} números")