#import traceback
def calculator():
    
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        d_age = float(age)

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
    
        if d_age < 0:
            print('Age cannot be a negative number')
        else:
            if d_age > 5:
                h_age = round(((5 * 7.2)+(d_age-5)*7), 2)
            elif d_age > 4:
                h_age = round(d_age * 7.2, 2)
            elif d_age > 3:
                h_age = round(d_age * 8, 2)
            elif d_age > 2:
                h_age = round(d_age * 9.3, 2)
            elif d_age > 1:
                h_age = round(d_age * 12, 2)
            else:
                h_age = round(d_age * 15, 2)

            print("\"The given dog age {} is {} in human years\"".format(age,h_age))
    except:
        print(age, "is an invalid age.")
        #print(traceback.format_exc())
    
calculator() # This line calls the calculator function