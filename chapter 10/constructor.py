class Employee:
    language = "Python"# This is class attribute.
    salary = 65000

    def __init__(self,name,salary,language): #dunder method which auomatically called.
        self.name=name
        self.salary=salary
        self.language=language
        print("I am create an object.")

    def getInfo(self):
        print(f"The language is {self.language}.\nThe salary is {self.salary}")
    
    @staticmethod
    def greet(self):
        print("Good morning.")

heel = Employee("Heel", 120000, "Java")
heel.name = "Heel"
print(heel.name, heel.salary, heel.language)