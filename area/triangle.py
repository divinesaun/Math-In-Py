def triangle():
    try:
        base = eval(input('Enter The Base: '))
        height = eval(input('Enter The Height: '))
        area = base * height / 2

        print(f'\nThe Area Is: {area}')
    except NameError:
        print('Please Enter A Number, Rerun The Program And Try Again')
    except SyntaxError:
        print('Please Enter A Number, Rerun The Program And Try Again')
