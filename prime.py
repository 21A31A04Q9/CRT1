def is_prime():
    n=int(input("enter a number:"))
    for i in range(2,n):
          if n%i==0:
              print("not prime")
              break
    else:
        print("prime")
is_prime()
        






def avg():
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    c=int(input("enter c value"))
    sum=(a+b+c)/3
    print(sum)

avg()

def avg(a,b,c):
    print((a+b+c)/3)
avg(5,6,8)
