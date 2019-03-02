#94
n,k= map(int, input().split())
l=[]
for i in range(1,n+1):
    a=int(input(""))
    l.append(a)
for x in range(1,n+1):
    if(k==x):
        print(l[x-1])
