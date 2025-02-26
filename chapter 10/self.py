class Employee:
    language = "Python"# This is class attribute.
    salary = 65000

    def getInfo(self):
        print(f"The language is {self.language}.\nThe salary is {self.salary}")
    
    @staticmethod
    def greet(self):
        print("Good morning.")

heel = Employee()
heel.language = "Javascript" # This is instance attribute.
heel.greet()
# heel.getInfo()
Employee.getInfo(heel)