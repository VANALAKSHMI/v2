#57
n=int(input(""))
k=int(input(""))
l=[]
d=0
for i in range(0,n):
    a=int(input(""))
    l.append(a)
for x in l:
    if(x==k):
        d=d+1
print(d)
