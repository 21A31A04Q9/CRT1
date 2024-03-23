def login():
    n=1
    while(n>0):
        username=input("enter ")
        password=input("enter")
        if(username==password):
            print("success")
            break
        else:
            n=n+1
            print("invalid")
            
login()
    
