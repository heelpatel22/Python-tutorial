class Employee:
    company = "ITC"
    name = "Heel"
    def show(self):
        print(f"The name is {self.name} and the compony is {self.company}")

class Coder:
    language = "Python"
    def printlanguage(self):
        print(f"Out of all the language here is your language: {self.language}")


class Programmer(Employee,Coder):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printlanguage()
b.showlanguage()