from discount import discount
from percentage_xy import percentage_xy
from simple_perc import simple_percentage
from val_increase import increase
from percentage_inc import percentage_increase

choose_percent = input('(A) - For Discount (100 - 25% = 75)\n'
                       '(B) - For Increase (100 + 25% = 125\n'
                       '(C) - For Simple Percentage (25% of 100 = 25)\n'
                       '(D) - For Percentage of X from Y (25% of 100 = 25)\n'
                       '(E) - For Percentage Increase/Decrease (From 25 to 100 there is a 300% increase)\n\n')

choose_percent = choose_percent.lower()

if choose_percent == 'a':
    discount()
elif choose_percent == 'b':
    increase()
elif choose_percent == 'c':
    simple_percentage()
elif choose_percent == 'd':
    percentage_xy()
elif choose_percent == 'e':
    percentage_increase()
else:
    print('Your Input Is Invalid, Please Rerun The Program')
