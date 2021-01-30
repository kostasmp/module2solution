import os, time

run = True


def main_menu():
    

    os.system('Calculator.py')
    print("-------------------------------"
          "| ****************************|"
          "| Calculator - Made By Kostas |"
          "|-----------------------------|")





def operations_list():
    print("+.......Addition")
    print("-.......Subtraction")
    print("*.......Multiplication")
    print("/.......Division")
    print("^.......Powers")
    print("+.......Addition")
    print("/-.......Square Root")
    print("gcd.......Greatest Common Divisor(WARNING!!! ENTER INTEGERS ONLY, OR ELSE THE PROGRAM BREAKS)")
    print("flr.......Round Down A Number To The Nearest Integer(WARNING!!! ENTER INTEGERS ONLY, OR ELSE THE PROGRAM BREAKS)")
    print("d/r.......degrees to radians")
    print("r/d.......radians to degrees")
    print("Abs.......Absolute Value")
    print("log.......Returns the Appropriate log of the Input(user's input is the log power")
    print("e.......Returns 'e'")
    print("e^x.......Returns 'e' Raised to User's Input ")
    print("//.......Divide with Integral")
    print("P.......Returns PI(π)")
    print("tau.......Returns tau(2*PI)")
    print("sin.......Sine")
    print("cos.......Cosine")
    print("tan.......Tangent")
    print("E.......Exit")

def quit():

        time.sleep(0.8)
        print("Thank you for using this calculator")
        run = False



print("Press L to show list with operations")
print("Press E to exit")



abilities = input(" ")





if abilities == "L":
    operations_list()

while run == True:

 op = input("Choose an operation from the above list: ")

 if op == "E":
    run = False
    quit()





 if op == "+":
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        print(a + b)
    except:
        print("Invalid Input!")




 if op == "-":
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        print(a - b)
    except:
        print("Invalid Input!")



 if op == "*":
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        print(a * b)
    except:
        print("Invalid Input!")




 if op == "/":
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        print(a / b)
    except:
        print(ZeroDivisionError , 'Cannot divide numbers by 0')


 if op == "^":
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    from math import pow
    pow(a, b)
    print(pow(a, b))


 if op == "/-":
    a = float(input("Enter a number: "))
    if a > 0 or a == 0:
        try:
            from math import sqrt
            sqrt(a)
            print(sqrt(a))
        except:
            print("NO NUMBER ERROR: Negative Numbers Don't Have Square Root")

 if op == "gcd":
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    from math import gcd
    gcd(a, b)
    print(gcd(a, b))

 if op == "flr":
    a = int(input("Enter a number: "))
    from math import floor
    floor(a)
    print(floor(a))



 if op == "d/r":
    a = float(input("Enter a number: "))
    from  math import radians
    radians(a)
    print(radians(a))

 if op == "r/d":
    a = float(input("Enter a number: "))
    from math import degrees
    degrees(a)
    print(degrees(a))

 if op == "Abs":
    a = float(input("Enter a number: "))
    from math import fabs
    fabs(a)
    print(fabs(a))


 if op == "log":
    a = float(input("Enter a number: "))

    try:
        if a > 0 :
            from  math import log
            log(a)
            print(log(a))
    except:
        print("Section Error: Input cannot be 0 or lower!")




 if op == "e":
    import math
    print(math.e)

 if op == "e^x":
    a = float(input("Enter a number: "))
    from math import exp
    exp(a)
    print(exp(a))

 if op == "//":
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    if b != 0:
        try:
            from math import remainder
            remainder(a, b)
            print(remainder(a, b))
        except:
            print(ZeroDivisionError, "Cannot divide numbers by 0")



 if op == "P":
    import math
    print(math.pi)

 if op == "tau":
    import math
    print(math.tau)

 if op == "sin":
    a = float(input("Enter a number: "))
    from math import sin
    sin(a)
    print(sin(a))



 if op == "cos":
    a = float(input("Enter a number: "))
    from math import  cos
    cos(a)
    print(cos(a))




 if op == "tan":
    a = float(input("Enter a number: "))
    from math import tan
    tan(a)
    print(tan(a))

 









































