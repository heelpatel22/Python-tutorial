a = int(input("Enter a number: "))
b = int(input("Enter b number: "))

if(b == 0):
    raise ZeroDivisionError("not divisible")
else:
    print(f"the division a/b is {a/b}")