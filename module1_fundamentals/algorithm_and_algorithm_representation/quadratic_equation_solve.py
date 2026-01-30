import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Many roots exist")
        else:
            print("No roots exist")
    else:
        root = -c / b 
        print(f"Root is: ", root)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("No real roots exist")
    elif delta == 0:
        root = -b/(2*a)
        print(f"One real root exist: ", root)
    else:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Two real roots exist: ", root1, " and ", root2)
        