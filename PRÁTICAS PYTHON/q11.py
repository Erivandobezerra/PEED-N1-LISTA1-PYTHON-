print('CALCULAR NPUMEROS PARES')
pares = []

for i in range(1, 11):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
        
print('Os números pares são: ')
for num in pares:
    print(num)
