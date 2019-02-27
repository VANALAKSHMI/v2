#80
n=int(input(""))
r=0
c=0
l=[]
while(n>0):
    a=n%10
    if(a%2!=0):
       l.append(a)
       c=c+1
    n=n//10
for x in range(c-1,-1,-1):
    print(l[x],end=" ")
    
