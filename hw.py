n=1
for i in range(1,6):
    for j in range(1,1+i):
        print(i,end=" ")
    print()
for i in range(1,5):
    for j in range(1,6-i):
        print(5-i,end=" ")
        n=n-1
    print()
