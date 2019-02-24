#75
n=input("")
l=list(n)
rev=""
if(len(l)%2==0):
    a=len(l)//2
    l[a]='*'
    l[a-1]='*'
    for i in range(0,len(l)):
        rev=rev+l[i]
    print((rev))
if(len(l)%2!=0):
    a=len(l)//2
    l[a]='*'
    for i in range(0,len(l)):
        rev=rev+l[i]
    print((rev))
