def discount():
    print('Discount\n')
    try:
        initial_value = eval(input('Initial Value: '))
        percent = eval(input('Discount Percentage: '))
        disc = percent / 100 * initial_value

        print('\nThe Final Value Is: ${:.2f}\n'.format(initial_value - disc))
        print('The Discount: ${:.2f}'.format(disc))
    except NameError:
        print('Please Enter A Number, Rerun The Program And Try Again')
    except SyntaxError:
        print('Please Enter A Number, Rerun The Program And Try Again')
