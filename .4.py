a=int(input("enter 1 sub marks:"))
b=int(input("enter 2 sub marks:"))
c=int(input("enter 3 sub marks:"))
if(a>80 and b>80 and c>80):
    print("A+")
elif(60<(a and b and c)<80):
    print("B+")
else:
    print("Pass")
