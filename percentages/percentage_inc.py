def percentage_increase():
    print('Percentage Increase/Descrease\n')
    try:
        start_range = eval(input('From: '))
        finish_range = eval(input('To: '))
        perc_inc = (finish_range - start_range) * (finish_range / start_range)

        print(f'\nThe Percentage Increase: {perc_inc}%')
    except NameError:
        print('Please Enter A Number, Rerun The Program And Try Again')
    except SyntaxError:
        print('Please Enter A Number, Rerun The Program And Try Again')
