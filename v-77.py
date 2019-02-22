#67
n=int(input(""))
if(n<=10000):
    while(n>0):
        n=n+1
        if(n%10==0):
            print(n)
            n=0
else:
    print("invalid")
            
