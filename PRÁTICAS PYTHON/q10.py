print('CALCULADORA DE MÉDIA')
soma = 0

for i in range(1,6):
    num = int(input('Digite um número: '))
    soma = soma + num
media = soma/5

print('A média da soma anterior é: ', media)
