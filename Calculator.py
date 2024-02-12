while True:
    operation=input("Select Operator: +, -, *, **, /, //, %, break (stop) ")
    if operation!="break":
        first_number=float(input("Select First Number: "))
        second_number=float(input("Select Second Number:  "))
        if operation=="+":
            print(float(first_number+second_number))
        elif operation=="-":
            print(float(first_number-second_number))   
        elif operation=="*":
            print(float(first_number*second_number))
        elif operation=="**":
            print(float(first_number**second_number))
        elif operation=="/":
            print(float(first_number/second_number))    
        elif operation=="//":
            print(float(first_number//second_number))    
        elif operation=="%":
            print(float(first_number%second_number))    
        else:
            print("Invalid Operator")
            continue
    elif operation=="break":
        print("Exiting")
        break