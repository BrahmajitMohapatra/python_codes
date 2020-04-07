import random
class ValueTooSmallError(Exception):
    pass
class ValueTooLargeError(Exception):
    pass
number= random.randint(1,100)
while True :
    try:
        i_num = int (input("Enter the number = "))
        if i_num < number :
            raise ValueTooSmallError
        elif i_num > number :
            raise ValueTooLargeError
        break
    except(ValueTooSmallError):
        print("This Value is Too small Try again ")
    except(ValueTooLargeError):
        print("This Value is Too Large Try again ")
print("Congratulations !!!! You Guessed it correctly.")             
