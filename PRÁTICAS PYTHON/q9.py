print('Menor número!')
menor = ''

for i in range(1,6):
    num = (input('Informe um número: '))
    if len(num) > len(menor):
        menor = num
print('Menor número: ', menor)