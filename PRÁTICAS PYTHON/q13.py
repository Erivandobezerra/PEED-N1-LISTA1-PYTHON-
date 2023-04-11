lista_p = []
for i in range(1, 6):
    palavra = input('Informe uma palavra: ')

    lista_p.append(palavra)

print("As palavras iniciadas com 'aA' o são: ")
for palavra in lista_p:
    if palavra[0] == 'a' or palavra[0] == 'A':
        print(palavra)
