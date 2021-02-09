#get the factorial of a number

def factorial_iterativo(number):
    fact = 1
    for i in range(1, number +1):
        fact *= i
    return fact

def factorial_recursivo(number):
    if number == 0:
        return 1
    else:
        return number*factorial_recursivo(number-1)

number = int(input("Número: "))

if number>=0:
    print('El factorial recursivo es: ', factorial_recursivo(number))
    print('El factorial iterativo es: ', factorial_iterativo(number))

else:
    print('Número no válido')
