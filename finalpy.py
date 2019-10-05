
def addition( ):
    num1 =input("Enter first number for addition : ")
    num2 =input("Enter second number for addition : ")
    re5s =float(num1 ) +float(num2)
    print("Result : " +str(num1) + " + " + str(num2) + " = " + str(res))


def subtraction():
    num1 = input("Enter first number for subtraction : ")
    num2 = input("Enter second number for subtraction : ")
    res = float(num1) - float(num2)
    print("Result : " + str(num1) + " - " + str(num2) + " = " + str(res))


def multiplication():
    num1 = input("Enter first number for multiplication : ")
    num2 = input("Enter second number for multiplication : ")
    res = float(num1) * float(num2)
    print("Result : " + str(num1) + " * " + str(num2) + " = " + str(res))


def division():
    num1 = int(input("Enter dividend : "))
    num2 = int(input("Enter divisor : "))
    if num2 == 0:
        print("Zero division error ")
    else:
        res = num1 / num2
        mod = num1 % num2
        print("Result : " + str(num1) + " / " + str(num2) + " = " + str(res))
        print("Remainder of above division = " + str(mod))


def power():
    num1 = int(input("Enter any number : "))
    p = int(input("Enter power for the above number for calculatio : "))
    res = num1 ** p
    print("Result : " + str(num1) + " raise to the power " + str(p) + " = " + str(res))


def square_root():
    num1 = int(input("Enter number whose square root you want to calculate :"))
    res = (num1) ** 0.5
    if res < 0:
        print("This calculator does not show result in imaginary values")
    else:
        print("Result : Square root of " + str(num1) + " = " + str(res))


import math


def sine_function():
    x = input("Enter value : ")
    x = float(x)
    ans = math.sin(x)
    print("The Sine of ", x, " is ", float(ans))


def cos_function():
    x = input("Enter value : ")
    x = float(x)
    ans = math.cos(x)
    print("The Cos of ", x, "is", float(ans))


def tan_function():
    x = input("Enter value : ")
    x = float(x)
    ans = math.tan(x)
    print("The Tan of ", x, "is", float(ans))


def cosec_function():
    x = input("Enter value : ")
    x = float(x)
    ans = (1 / math.sin(x))
    print("The Cosec of ", x, "is", float(ans))


def sec_function():
    x = input("Enter value : ")
    x = float(x)
    ans = (1 / math.cos(x))
    print("The Sec of ", x, "is", float(ans))


def cot_function():
    x = input("Enter value : ")
    ans = (1 / math.tan(x))
    print("The Cot of ", x, "is", float(ans))


def degree_to_radians():
    x = input("Enter value : ")
    x = float(x)
    ans = math.radians(x)
    print("The radian of ", x, " is ", float(ans))


def radians_to_degree():
    x = input("Enter value : ")
    x = float(x)
    ans = math.degrees(x)
    print("The degree of ", x, " is ", float(ans))


def value(num):
    x = bin(num)
    print(" The number conversion is=", x)


def value1(num1):
    x1 = oct(num1)
    print(" The number conversion is= ", x1)


def value2(num2):
    x2 = hex(num2)
    print(" The number conversion is=", x2)


def value3(num3):
    x3 = int(num3, 2)
    print("The number conversion is=", x3)


def value4(num4):
    x4 = hex(int(num4, 2))
    print("The number conversion is=", x4)


def value5(num5):
    x5 = oct(int(num5, 2))
    print(" The number conversion is=", x5)


def value6(num6):
    x6 = int(num6, 8)
    print(" The number conversion is=", x6)


def value7(num7):
    x7 = int(num7, 16)
    print(" The number conversion is= ", x7)


def value8(num8):
    x8 = bin(int(num8, 8))
    print(" The number conversion is= ", x8)


def value9(num9):
    x9 = bin(int(num9, 16))
    print(" The number conversion is= ", x9)


def value10(num10):
    x10 = hex(int(num10, 8))
    print(" The number conversion is= ", x10)


def value11(num11):
    x11 = oct(int(num11, 16))
    print(" The number conversion is= ", x11)


def find_factorial(n):
    f = 1
    n=int(n)
    if n == 1 or n == 0:
        return 1
    else:
        for k in range(1, n + 1):
            f = f * k
    return f


def exponential():
    import math
    n = int(input("Enter the number of terms: "))
    sum1 = 1
    for i in range(1, n + 1):
        sum1 = sum1 + (1 / math.factorial(i))
    print("The sum of series is", round(sum1, 2))


def find_npr():
    nval = int(input("enter value of n :"))
    rval = int(input("enter value of r :"))
    result = factorial(nval) / factorial(nval - rval)
    print("The permutation of given values = " + str(result))


def find_ncr():
    nval = int(input("enter value of n :"))
    rval = int(input("enter value of r :"))
    result = factorial(nval) /(factorial(nval- rval)*factorial(rval))
    print("The combination of given values = " + str(result))


def Not():
    print("NOT OPERATOR")
    print(" Enter any binary number")
    a = int(input(""))
    if a < 0 or a > 1:
        print(" Invalid Input ")
        exit()
    else:
        if a == 0:
            res = 1
        else:
            res = 0
    print(res)


def Or():
    print("OR OPERATOR")
    print(" Enter first binary number")
    a = int(input(""))
    print(" Enter second binary number")
    b = int(input(""))
    if a < 0 or a > 1 or b < 0 or b > 1:
        print(" Invalid Input ")
        exit()
    else:
        res = a + b
        if res > 1:
            res = 1
    print(res)


def Nor():
    print("NOR OPERATOR")
    print(" Enter first binary number")
    a = int(input(""))
    print(" Enter second binary number")
    b = int(input(""))
    if a < 0 or a > 1 or b < 0 or b > 1:
        print(" Invalid Input ")
        exit()
    else:
        res = a + b
        if res > 1:
            res = 1
    res = res + 1
    if res > 1:
        res = 0
    print(res)


def And():
    print("AND OPERATOR")
    print(" Enter first binary number")
    a = int(input(""))
    print(" Enter second binary number")
    b = int(input(""))
    if a < 0 or a > 1 or b < 0 or b > 1:
        print(" Invalid Input ")
        exit()
    else:
        res = a * b
    print(res)


def nand():
    print("NAND OPERATOR")
    print(" Enter first binary number")
    a = int(input(""))
    print(" Enter second binary number")
    b = int(input(""))
    if a < 0 or a > 1 or b < 0 or b > 1:
        print(" Invalid Input ")
        exit()
    else:
        res = a * b
    res = res + 1
    if res > 1:
        res = 0
    print(res)


def xor():
    print("XOR OPERATOR")
    print(" Enter first binary number")
    a = int(input(""))
    print(" Enter second binary number")
    b = int(input(""))
    if a < 0 or a > 1 or b < 0 or b > 1:
        print(" Invalid Input ")
        exit()
    else:
        if a == b:
            res = 0
        else:
            res = 1
    print(res)


def xnor():
    print("XNOR OPERATOR")
    print(" Enter first binary number")
    a = int(input(""))
    print(" Enter second binary number")
    b = int(input(""))
    if a < 0 or a > 1 or b < 0 or b > 1:
        print(" Invalid Input ")
        exit()
    else:
        if a == b:
            res = 0
        else:
            res = 1
    res = res + 1
    if res > 1:
        res = 0
    print(res)


choice = ''
while choice != 'EXIT':
    print("To close the calculator Type EXIT")
    print("To perform Arithmetic operation Type 1")
    print("To perform Trigonometric operations Type 2")
    print("To perform Logic operations i.e AND,OR,NOT.. Type 3")
    print("To perform conversions of number system Type 4")
    print("If you want to perform any other function Enter 5")
    choice = input()
    if choice == '1':
        opt = input("kindly enter which arithmetic operation you want to perform?")
        if opt == '+' or opt == 'Add' or opt == 'add' or opt == 'ADD':
            addition()
        elif opt == '-' or opt == 'sub' or opt == 'Sub' or opt == 'SUB':
            subtraction()
        elif opt == '*' or opt == 'multiply' or opt == 'Multiply' or opt == 'MULTIPLY':
            multiplication()
        elif opt == '/' or opt == 'divide' or opt == 'Divide' or opt == 'DIVIDE':
            division()
        elif opt == 'power' or opt == 'notation' or opt == 'POWER' or opt == 'Power':
            power()
        elif opt == 'square root' or opt == 'Square Root' or opt == 'Square root' or opt == 'SQUARE ROOT':
            square_root()
        else:
            print("invalid input")
    elif choice == '2':
        opt = input("kindly enter which trigonometric operation you want to perform?")
        if opt == 'sin' or opt == 'Sin' or opt == 'Sine' or opt == 'sine':
            sine_function()
        elif opt == 'cos' or opt == 'Cos' or opt == 'cosec' or opt == 'Cosec':
            cos_function()
        elif opt == 'tan' or opt == 'tangent' or opt == 'Tan' or opt == 'Tangent':
            tan_function()
        elif opt == 'cosec' or opt == 'Cosec':
            cosec_function()
        elif opt == 'sec' or opt == 'Sec':
            sec_function()
        elif opt == 'cot' or opt == 'Cot':
            cot_function()
        else:
            print("Invalid operation")
    elif choice == '3':
        opt = input("Enter which Logical operation you want to perform?")
        if opt == 'OR' or opt == 'Or' or opt == 'or' or opt == '|' or opt == '||':
            Or()
        elif opt == 'AND' or opt == 'And' or opt == 'and' or opt == '&' or opt == '&&':
            And()
        elif opt == 'NOT' or opt == 'Not' or opt == 'not' or opt == '~':
            Not()
        elif opt == 'NOR' or opt == 'Nor' or opt == 'nor':
            Nor()
        elif opt == 'NAND' or opt == 'Nand' or opt == 'nand':
            nand()
        elif opt == 'XNOR' or opt == 'Xnor' or opt == 'xnor':
            xnor()
        elif opt == 'XOR' or opt == 'xor' or opt == 'Xor':
            xor()
        else:
            print("Invalid Input")
    elif choice == '4':
        choice = " "
        print(" PRESS 1 TO CONVERT DECIMAL INTO BINARY")
        print(" PRESS 2 TO CONVERT DECIMAL INTO HEXADECIMAL")
        print(" PRESS 3 TO CONVERT DECIMAL INTO OCTAL")
        print(" PRESS 4 TO CONVERT BINARY INTO DECIMAL")
        print(" PRESS 5 TO CONVERT BINARY INTO HEXADECIMAL")
        print(" PRESS 6 TO CONVERT BINARY INTO OCTAL")
        print(" PRESS 7 TO CONVERT OCTAL INTO DECIMAL")
        print(" PRESS 8 TO CONVERT HEXADECIMAL INTO DECIMAL")
        print(" PRESS 9 TO CONVERT OCTAL INTO BINARY")
        print(" PRESS 10 TO CONVERT HEXADECIMAL INTO BINARY ")
        print(" PRESS 11 TO CONVERT OCTAL INTO HEXADECIMAL")
        print(" PRESS 12 TO CONVERT HEXADECIMAL INTO OCTAL")
        while choice != 13:
            choice = int(input(" ENTER YOUR CHOICE:  "))
            if choice == 1:
                a = int(input("ENTER ANY NUMBER : "))
                value(a)
            elif choice == 2:
                b = int(input(" ENTER ANY NUMBER : "))
                value1(b)
            elif choice == 3:
                c = int(input("ENTER ANY NUMBER : "))
                value2(c)
            elif choice == 4:
                d = input(" ENTER BINARY NUMBER : ")
                value3(d)
            elif choice == 5:
                e = input(" ENTER BINARY NUMBER: ")
                value4(e)
            elif choice == 6:
                f = input(" ENTER BINARY NUMBER : ")  # value like: 111111
                value5(f)
            elif choice == 7:
                g = input(" ENTER OCTAL NUMBER: ")  # value like: 0o117
                value6(g)
            elif choice == 8:
                h = input(" ENTER ANY HEXADECIMAL NUMBER: ")  # value like: 0x4f
                value7(h)
            elif choice == 9:
                i = input(" ENTER ANY OCTAL NUMBER:  ")  # value like: 0o117
                value8(i)
            elif choice == 10:
                j = input(" ENTER ANY HEXADECIMAL NUMNER: ")  # value like: 45ab
                value9(j)
            elif choice == 11:
                k = input(" ENTER ANY OCTAL NUMBER: ")  # value like: 0o117
                value10(k)
            elif choice == 12:
                l = input(" ENTER ANY HEXADECIMAL NUMBER: ")  # value like: 0x27e
                value11(l)
            else:
                print("  ERROR! INVALID CHOICE")
    elif choice == '5':
        opt = input("Enter which operation you want to perform?")
        if opt == 'factorial' or opt == 'Factorial' or opt == 'fact' or opt == 'Fact' or opt == '!':
            num = int(input("Enter number to find factorial : "))
            resoffact=find_factorial(num)
            print("the factorial of given number is" +resoffact)

        elif opt == 'exponent' or opt == 'exponential' or opt == 'e':
            exponential()
        elif opt == 'nCr' or opt == 'ncr' or opt == 'NCR' or opt == 'combination':
            find_ncr()
        elif opt == 'nPr' or opt == 'npr' or opt == 'NPR' or opt == 'permutation':
            find_npr()
        else:
            print("Sorry! This calculator does not perform " + opt)
    else:
        print("Invalid Input")

