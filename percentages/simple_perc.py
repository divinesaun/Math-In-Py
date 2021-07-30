def simple_percentage():
    print('Simple Percentage\n')
    try:
        percent = eval(input('Enter The Percentage: '))
        value = eval(input('Enter The Value: '))

        print(f'\n{percent}% of {value} = {percent / 100 * value}')
    except NameError:
        print('Please Enter A Number, Rerun The Program And Try Again')
    except SyntaxError:
        print('Please Enter A Number, Rerun The Program And Try Again')
