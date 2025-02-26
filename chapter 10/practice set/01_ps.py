class programmer:
    company = "Google"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p = programmer("Heel", 100000, 384001)
print(p.name,p.salary,p.company,p.pin)