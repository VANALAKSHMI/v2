#24-TO FIND SORTED LIST
l=[]
n=int(input("N="))
if(1<=n<=1000):
    print("enter your ",n,"integers")
    for x in range(1,n+1):
        a=int(input(""))
        l.append(a)
    print(l)
    for x in range(len(l)):
        for y in range(x,len(l)):
             if(l[x]>l[y]):
                l[x],l[y]=l[y],l[x]
    print("sorted list",l)
else:
    print("invalid input")
