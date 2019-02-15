#57
n=int(input(""))
k=int(input(""))
l=[]
c=0
for i in range(0,n):
    a=int(input(""))
    l.append(a)
print(l)
for i in l:
    if(i==k):
        c=c+1
print(c)
