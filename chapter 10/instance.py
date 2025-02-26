class Employee:
    language = "Python"# This is class attribute.
    salary = 65000

heel = Employee()
heel.language = "Javascript" # This is instance attribute.
print(heel.language,heel.salary)