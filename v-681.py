#58
n=int(input(""))
k=int(input(""))
l=[]
d=0
for i in range(0,n):
    a=int(input(""))
    l.append(a)
for i in l:
    if(i==k):
        d=d+1
if(d>=1):
    print("Yes")
else:
    print("no")
