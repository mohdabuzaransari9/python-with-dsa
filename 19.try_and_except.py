def divide(divide_by_number):
    try: 
        divisor=25
        remainder=divisor/divide_by_number
        print(remainder)
        return remainder

    except:
        pass
        print("you divide a number by zero")   

divide(5)
divide(0)
#abnormal termination of program
#ZeroDivisionError: division by zero
#to run whole program smooth function we use try and except
divide(1)