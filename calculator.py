try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What kind of operation do you want to perform?" \
        "\n+ for Addition\n- for Subtraction\n* for Multiplication\n/ for divison")

    o=input("Enter Opearation: ")
    match o:
        case "+":
            print(f"The result is: {a+b}")
        case "-":
            print(f"The result is: {a-b}")
        case "*":
            print(f"The result is: {a*b}")
        case "/":
            print(f"The result is: {a/b}")
        case default:
            print(f"There was an error")
except Exception as e:
    print("Enter a valid value of a and b")
