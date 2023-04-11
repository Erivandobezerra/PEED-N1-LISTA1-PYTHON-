print('Maior número!')
maior = ''

for i in range(1,6):
    num = (input('Informe um número: '))
    if len(num) > len(maior):
        maior = num
print('Maior número: ', maior)