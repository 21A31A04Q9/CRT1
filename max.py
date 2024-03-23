a=[42,36,28,96,4,-1,1]
b=max(a)+min(a)
print(b)


a=[42,36,28,96,4,-1,1]
min=999
max=-999
for i in range(0,len(a)):
  if a[i]<min:
    min=a[i]
  if a[i]>max:
    max=a[i]
print(max+min)

