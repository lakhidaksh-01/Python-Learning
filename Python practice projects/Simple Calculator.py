# Simple Python Calculator


def calulator():
    Num1=float(input("enter the first number:"))
    Num2=float(input("enter the second number:"))
    print("Select Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operator=input("Enter choice (1/2/3/4): ")

    if operator == "1":
        result=Num1+Num2
        print(round(result,3))
    elif operator == "2":
        result=Num1-Num2
        print(round(result,3))
    elif operator == "3":
        result=Num1*Num2
        print(round(result,3))
    elif operator == "4":
        result=Num1/Num2
        print(round(result,3))
    else:
        print(f"{operator} is invaild operation")
        
    calulator()


if __name__ == "__main__":
    calulator()