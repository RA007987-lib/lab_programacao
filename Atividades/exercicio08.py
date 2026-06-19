frase = input("Digite uma frase: ")+" "
palavra_atual = ""
lista_palavra = []

for caractere in frase:
    if caractere !=" ":
        palavra_atual += caractere
    else:
        if palavra_atual!="":
            lista_palavra.append(palavra_atual)
            palavra_atual=""
        print(f"Vetor de palavras gerado: {lista_palavra}")
