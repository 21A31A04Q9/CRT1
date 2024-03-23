class F15:
    def light(self):
        print("ok switching on the light")
    def fan(self,speed):
        print("ok switching on the fan and speed is",speed)
        self.s=speed
    def cpu(self):
        print("on cpu")
        print(self.s)
chandhu=F15()
chandhu.light()
chandhu.fan(6)
chandhu.cpu()



class shopping:
    def dresstype(self,type):
        print("the dress type is",type)
        self.d=type
    def price(self,cost):
        print("the cost is",cost)
        self.c=cost
    def size(self,si):
        print("the size is",si)
        self.s=si
    def display(self):
        print(self.d,self.c,self.s)
priya=shopping()
priya.dresstype("shorts")
priya.price(2500)
priya.size("M")
priya.display()


class shopping:
    def __init__(self,place):
        self.z=place
        print("Welcome to shopping at",place)
    def dresstype(self,type):
        print("the dress type is",type)
        self.d=type
    def price(self,cost):
        print("the cost is",cost)
        self.c=cost
    def size(self,si):
        print("the size is",si)
        self.s=si
    def display(self):
        print(self.d,self.c,self.s,self.z)
priya=shopping("zudio")
priya.dresstype("shorts")
priya.price(2500)
priya.size("M")
priya.display()


class F15:
    def light(self):
        print("ok switching on the light")
    def fan(self,speed):
        print("ok switching on the fan and speed is",speed)
        self.s=speed
    def cpu(self):
        print("on cpu")
        print(self.s)

class shopping(F15):
    def __init__(self,place):
        self.z=place
        print("Welcome to shopping at",place)
    def dresstype(self,type):
        print("the dress type is",type)
        self.d=type
    def price(self,cost):
        print("the cost is",cost)
        self.c=cost
    def size(self,si):
        print("the size is",si)
        self.s=si
    def display(self):
        print(self.d,self.c,self.s,self.z)

class sub(shopping):
    def math(self,mar):
        self.e=mar
    def sci(self,a):
        self.i=a
    def d(self):
        print(self.e,self.i)
o=sub("zudio")
o.math(89)
o.sci(99)
o.price(2500)
o.fan(6)




