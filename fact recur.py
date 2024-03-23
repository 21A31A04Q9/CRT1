def f(n):
    if n==0:
        return 1
    return n*f(n-1)
a=f(6)
print(a)



def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
a=fib(5)
print(a)


def p(n,m):
    if m==0:
        return 1
    if n==0:
        return 0
    return n*p(n,m-1)
a=p(2,3)
print(a)
