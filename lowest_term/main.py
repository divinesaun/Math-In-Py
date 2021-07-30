numerator = int(input('Enter Numerator: '))
denominator = int(input('Enter Denominator: '))
for i in range(numerator, 0, -1):
    if (numerator % i == 0) and (denominator % i == 0):
        print('\nYour Fraction In Lowest/Simplest Terms =', sep='\n')
        print('{:^6d}\n{}\n{:^6d}'.format(int(numerator / i), '--------', int(denominator / i)))
        print(f'\nYour Fraction As A Simple Decimal = {round(numerator / denominator, 3)}')
        break
