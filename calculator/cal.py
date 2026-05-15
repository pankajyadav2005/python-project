try:
    a=int(input("enter value of a"))
    b=int(input("enter value of b"))

    print("which operation u want to perform. for addition press +\n for subtraction press -\n for multiplication press *\n for division press /")
    o=input("enter the operator").strip()
    match o:
        case "+":
            print(a+b)
        case "-":
            print(a-b)
        case "*":
            print(a*b)
        case "/":
            print(a/b)
        case _:
            print("invalid operator")   

except Exception as e: 
    print("give a valid number")   