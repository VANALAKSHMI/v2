
#22-TO FIND MAXIMUM ELEMENT
l=[]
n=int(input("N="))
if(1<=n<=100000):
    print("enter your ",n,"integers")
    for x in range(1,n+1):
        a=int(input(""))
        l.append(a)
    print(l)
    m=l[-1]
    s=l[-1]
    for x in l:
        if(m<x):
            m=x
    print("maximum:",m)
else:
    print("invalid input")
