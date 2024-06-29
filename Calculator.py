# Simple Calculator
x='y'

while x=='y':
    user_input=int(input("""enter the operation you want to perform :
                         1- Addition
                         2- Subtraction
                         3- Division
                         4- Multiplication
                         5- Exponential
                         6- Modulus \n"""))
    a=int(input("enter first value"))
    b=int(input("enter second value"))
    if(user_input ==1):
        print("Addition",a+b)
    elif(user_input==2):
        if(a>b):
            print("Subtraction",a-b)
        else:
            print("invalid value!!")
    elif(user_input==3):
        print("Division",a/b)
    elif(user_input==4):
        print("Multiplication",a*b)
    elif(user_input==5):
        print("Exponential",a**b)
    elif(user_input==6):
         print("Modulus",a%b)
    else:
        print("Inavlid Input!! Please enter valid value")
    x=input("press y to roll again and n to exit:")
    print("\n")
