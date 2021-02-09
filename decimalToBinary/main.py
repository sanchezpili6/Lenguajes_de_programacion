decimal = int(input('Number you want to make binary: '))
binary = ''
while decimal != 0:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2
print(f'Your number in binary is: {binary}')


