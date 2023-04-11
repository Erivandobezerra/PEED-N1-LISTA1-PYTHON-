print('CALCULAR NPUMEROS IMPARES')
impar = []

for i in range(1, 11):
    num = int(input('Digite um número: '))
    if num % 2 != 0:
        impar.append(num)
        
print('Os números ímpares são: ')
for num in impar:
    print(num)
