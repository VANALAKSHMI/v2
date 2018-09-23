#26-TO FIND SORTED LIST
l=[]
n=int(input("N="))
if(1<=n<=100000):
    print("enter your ",n,"integers")
    for x in range(1,n+1):
        a=int(input(""))
        l.append(a)
    print(l)
    def part(ml,s,e):
     p=ml[s]
     lt=s+1
     rt=e
     done=False
     while not done:
        while lt<=rt and ml[lt]<=p:
            lt=lt+1
        while ml[rt]>=p and rt>=lt:
            rt=rt-1
        if rt<lt:
            done=True
        else:
            t=ml[lt]
            ml[lt]=ml[rt]
            ml[rt]=t
     t=ml[s]
     ml[s]=ml[rt]
     ml[rt]=t
     return rt
    def quick(ml,s,e):
     if s<e:
        p=part(ml,s,e)
        quick(ml,s,p-1)
        quick(ml,p+1,e)
     return ml
    print(quick(l,0,len(l)-1))
else:
    print("invalid input")





