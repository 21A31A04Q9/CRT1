sum1=0
sum2=0
for i in range(2,11):
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
print(sum1,sum2)


sum1=0
sum2=0
for i in range(1,31):
    if i%6==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
print(sum1,sum2)
H=sum1-sum2
print(H)





s=1
p=int(input("enter a value"))
for i in range(1,p+1):
    s=i*s
print(s)
      
