a = int(input("enter your age: "))

#if statement no: 1
if(a%2==0):
    print("a is even.")

#end of if no: 1

#if statement no: 2
if(a>=18):
    print("You are eligible.")
elif(a<0):
    print("Invalid.")
elif(a==0):
    print("You are 0.")
else:
    print("You are not eligible.")

#end of if no: 2

print('End of program.')