class a:
    def b(self):
        print("ooo")
class c(a):
    def d(self):
        print("lll")
y=c()
y.b()
y.d()

class e(a):
    def f(self):
        print("MMM")
p=e()
p.b()
p.f()
