print('Descobrindo a palavra mais longa!')

longa = ''

for lista in range (1,6):
    palavra = str(input('Digite uma palavra: '))
    if len(palavra) > len(longa):
        longa = palavra
print('A palavra mais longa informada foi: ', longa)