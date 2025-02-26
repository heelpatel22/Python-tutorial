marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grades = "Ex"
elif(marks<90 and marks>=80):
    grades = "A"
elif(marks<80 and marks>=70):
    grades = "B"
elif(marks<70 and marks>=60):
    grades = "C"
elif(marks<60 and marks>=50):
    grades = "D"
elif(marks<50):
    grades = "F"

print("Your grade is: ",grades)