class Employee:
    def __init__(self):
        print("constructer of employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("constructer of programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("constructer of manager")
    c = 3

# o = Employee()
# print(o.a)
# print(o.b)

# o = Programmer()
# print(o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)