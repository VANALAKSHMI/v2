#77
n=int(input(""))
if(n<=1000):
    for x in range (1,n+1):
        if(n%x==0):
            print(x)
        
