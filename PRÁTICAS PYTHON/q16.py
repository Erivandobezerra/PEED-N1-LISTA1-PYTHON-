
pares = []
soma = 0

for i in range(1, 11):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
        soma = soma + num
        
print('Números pares informados: ')
for num in pares:
    print(num)
    
print('Soma: ', soma)