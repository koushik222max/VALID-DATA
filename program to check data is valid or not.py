while True:
    a=list(map(int,input('Enter the numbers seprated by numbers:').split(',')))

    valid=True

    for i in a:
        if i<0 or i>10 or i!=int:
            valid=False

    if valid:
        break

    else:
        if i==str:
            print('\nEnter only numbers')

        if i==float:
            print('\nEnter only intigers')

        if i<0 or i>10:
            print('\nEnter numbers less than 10')

        print('\nPlease enter correct input')
        print('')

print('The numbers are beautiful')

    
