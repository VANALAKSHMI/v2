#25-TO FIND MEDIAN ELEMENT IN THE SORTED LIST
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
    print("MEDIAN ELMENT:")
    length = len(l)
    if (length % 2 == 0):
        mid = (l[(length)//2] + l[(length)//2-1]) / 2
    else:
        mid = l[(length-1)//2]
    print(mid)
else:
    print("invalid input")
