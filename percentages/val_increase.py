def increase():
    print('Value Increase\n')
    try:
        initial_value = eval(input('Initial Value: '))
        percent = eval(input('Increase Percentage: '))
        inc = percent / 100 * initial_value

        print('\nThe Final Value Is: ${:.2f}\n'.format(initial_value + inc))
        print('The Increase: ${:.2f}'.format(inc))
    except NameError:
        print('Please Enter A Number, Rerun The Program And Try Again')
    except SyntaxError:
        print('Please Enter A Number, Rerun The Program And Try Again')
