n = int(input("enter a num: "))

for i in range(1,n):
    if(n%i)==0:
        print("Not prime")
        break
else:
    print("Prime")