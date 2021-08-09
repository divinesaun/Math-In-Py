def rectangle():
    try:
        length = eval(input('Enter The Length: '))
        width = eval(input('Enter The Width: '))
        area = length * width

        print(f'\nThe Area Is: {area}')
    except NameError:
        print('Please Enter A Number, Rerun The Program And Try Again')
    except SyntaxError:
        print('Please Enter A Number, Rerun The Program And Try Again')
