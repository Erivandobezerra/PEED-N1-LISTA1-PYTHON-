
menor5 = []

for i in range(1, 11):
    num = int(input('Digite um número: '))
    if num < 5:
        menor5.append(num)
        
print('números menores que 5 informados: ')
for num in menor5:
    print(num)