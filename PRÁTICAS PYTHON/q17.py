impar = []
soma = 0

for i in range(1, 11):
    num = int(input('Digite um número: '))
    if num % 2 != 0:
        impar.append(num)
        soma = soma + num
        
print('Números ímpares informados: ')
for num in impar:
    print(num)
    
print('Soma: ', soma)