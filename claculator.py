def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def calcul():
    print("1. add, 2.sub")
    c = input("choice: ")
    num1 = float(input("first number: "))
    num2 = float(input("second number: "))
    if c == '1':
        print(f"{add(num1, num2)}")
    elif c == '2':
        print(f"{sub(num1, num2)}")
    else :
        print("Invalid input")
        
calcul()
