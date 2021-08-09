def square():
    try:
        side = eval(input('Enter The Side: '))

        print(f'\nThe Area Is: {side ** 2}')
    except NameError:
        print('Please Enter A Number, Rerun The Program And Try Again')
    except SyntaxError:
        print('Please Enter A Number, Rerun The Program And Try Again')
