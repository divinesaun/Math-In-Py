def percentage_xy():
    print('Percentage of X from Y\n')
    try:
        x = eval(input('Enter X: '))
        y = eval(input('Enter Y: '))

        print(f'\nThe Percentage: {round(x / y * 100, 2)}%')
    except NameError:
        print('Please Enter A Number, Rerun The Program And Try Again')
    except SyntaxError:
        print('Please Enter A Number, Rerun The Program And Try Again')
